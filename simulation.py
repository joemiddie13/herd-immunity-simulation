import random
import sys
from datetime import datetime
from person import Person
from logger import Logger
from virus import Virus
import matplotlib.pyplot as plt

class Simulation(object):
	def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
		"""
		Initialize a new Simulation instance.
		Args:
				virus (Virus): The virus to simulate.
				pop_size (int): Total population size.
				vacc_percentage (float): Percentage of the population that is vaccinated.
				initial_infected (int): Initial number of infected individuals.
		"""
		self.logger = Logger("simulation_log.txt")  # Logger instance for logging simulation data.
		self.virus = virus
		self.pop_size = pop_size
		self.vacc_percentage = vacc_percentage
		self.initial_infected = initial_infected
		self.population = self._create_population()  # Creating the initial population.
		self.current_step = 0
		self.total_interactions = 0
		self.total_deaths = 0
		self.total_vaccinated = sum(p.is_vaccinated for p in self.population)
		self.infections_over_time = []  # To track infections over time.
		self.deaths_over_time = []  # To track deaths over time.
		self.logger.write_metadata(pop_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate)

	def _create_population(self):
		"""
		Create the initial population for the simulation.
		Returns:
				List of Person objects representing the population.
		"""
		population = []
		num_vaccinated = int(self.pop_size * self.vacc_percentage)
		num_infected = self.initial_infected

		# Populating vaccinated, infected, and healthy individuals.
		for i in range(self.pop_size):
				if num_vaccinated > 0:
						population.append(Person(i, True))
						num_vaccinated -= 1
				elif num_infected > 0:
						population.append(Person(i, False, self.virus))
						num_infected -= 1
				else:
						population.append(Person(i, False))

		random.shuffle(population)  # Shuffling the population for randomness.
		return population

	def _simulation_should_continue(self):
		"""
		Check if the simulation should continue.
		Returns:
				bool: True if simulation should continue, False otherwise.
		"""
		living = sum(p.is_alive for p in self.population)
		return living > 0 and self.total_vaccinated < living

	def run(self):
		"""
		Run the simulation.
		"""
		while self._simulation_should_continue():
				new_infections, new_deaths = self.time_step()
				self.current_step += 1
				self.total_deaths += new_deaths
				self.infections_over_time.append(new_infections)
				self.deaths_over_time.append(new_deaths)
				self.logger.log_time_step(self.current_step, new_infections, new_deaths, self.current_population(), self.total_deaths, self.total_vaccinated)
		
		self.logger.write_final_summary(self.current_population(), self.total_deaths, self.total_vaccinated, "All living people have been vaccinated", self.total_interactions, self.total_vaccinated, self.percentage_infected(), self.percentage_deaths(), self.lives_saved())

	def time_step(self):
		"""
		Simulate one time step in the simulation.
		"""
		new_infections = 0
		new_deaths = 0
		interactions = 0

		for person in self.population:
				if person.infection:
						for _ in range(100):
								random_person = random.choice(self.population)
								if self.interaction(person, random_person):
										interactions += 1

						survived = person.did_survive_infection()
						if not survived:
								new_deaths += 1
						else:
								self.total_vaccinated += 1

		self.total_interactions += interactions
		return new_infections, new_deaths

	def interaction(self, infected_person, random_person):
		"""
		Simulate an interaction between two people.
		Args:
				infected_person (Person): The infected person in the interaction.
				random_person (Person): The random person who interacts with the infected person.
		"""
		if not random_person.is_vaccinated and random_person.infection is None:
				if random.random() < self.virus.repro_rate:
						random_person.infection = self.virus
						return True
		return False

	def current_population(self):
		"""
		Calculate the current population count.
		"""
		return sum(person.is_alive for person in self.population)

	def percentage_infected(self):
		"""
		Calculate the percentage of the population that became infected.
		"""
		infected = sum(p.infection is not None for p in self.population)
		return (infected / self.pop_size) * 100

	def percentage_deaths(self):
		"""
		Calculate the percentage of the population that died.
		"""
		return (self.total_deaths / self.pop_size) * 100

	def lives_saved(self):
		"""
		Calculate the number of lives saved by vaccinations.
		"""
		saved = sum(p.is_vaccinated and p.infection is None for p in self.population)
		return saved

def plot_simulation_results(infections, deaths):
	"""
	Plot the results of the simulation using matplotlib.
	Args:
			infections (list): A list of new infections at each time step.
			deaths (list): A list of new deaths at each time step.
	"""
	plt.figure(figsize=(10, 6))
	plt.plot(infections, label='New Infections')
	plt.plot(deaths, label='New Deaths')
	plt.xlabel('Time Steps')
	plt.ylabel('Number of Cases')
	plt.title('Virus Infection and Death Trends Over Time')
	plt.legend()
	plt.show()

if __name__ == "__main__":
	if len(sys.argv) != 7:
			print("Usage: python3 simulation.py population_size vaccination_percentage virus_name mortality_rate reproduction_rate initial_infected")
			sys.exit(1)

	population_size = int(sys.argv[1])
	vaccination_percentage = float(sys.argv[2])
	virus_name = sys.argv[3]
	mortality_rate = float(sys.argv[4])
	reproduction_rate = float(sys.argv[5])
	initial_infected = int(sys.argv[6])

	virus = Virus(virus_name, reproduction_rate, mortality_rate)
	simulation = Simulation(virus, population_size, vaccination_percentage, initial_infected)
	simulation.run()
	plot_simulation_results(simulation.infections_over_time, simulation.deaths_over_time)