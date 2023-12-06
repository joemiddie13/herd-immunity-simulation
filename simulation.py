import random
from datetime import datetime
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
	def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
		"""
		Initialize a new Simulation.
		Args:
				virus (Virus): The virus being simulated.
				pop_size (int): The total size of the population.
				vacc_percentage (float): The percentage of the population that is vaccinated.
				initial_infected (int): The initial number of infected individuals.
		"""
		self.logger = Logger("simulation_log.txt")
		self.virus = virus
		self.pop_size = pop_size
		self.vacc_percentage = vacc_percentage
		self.initial_infected = initial_infected
		self.population = self._create_population()
		self.current_step = 0
		self.total_interactions = 0
		self.total_deaths = 0
		self.total_vaccinated = sum(person.is_vaccinated for person in self.population)
		self.logger.write_metadata(pop_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate)

	def _create_population(self):
		"""
		Create the initial population for the simulation.
		Returns:
				list: A list of Person objects representing the population.
		"""
		population = []
		num_vaccinated = int(self.pop_size * self.vacc_percentage)
		num_infected = self.initial_infected

		for i in range(self.pop_size):
				if num_vaccinated > 0:
						population.append(Person(i, True))
						num_vaccinated -= 1
				elif num_infected > 0:
						population.append(Person(i, False, self.virus))
						num_infected -= 1
				else:
						population.append(Person(i, False))

		random.shuffle(population)
		return population

	def _simulation_should_continue(self):
		"""
		Determine if the simulation should continue.
		Returns:
				bool: True if the simulation should continue, False otherwise.
		"""
		living = sum(person.is_alive for person in self.population)
		return living > 0 and self.total_vaccinated < living

	def run(self):
		"""
		Run the simulation until it should no longer continue.
		"""
		while self._simulation_should_continue():
				new_infections, new_deaths = self.time_step()
				self.current_step += 1
				self.total_deaths += new_deaths
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
		infected = sum(person.infection is not None for person in self.population)
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
		saved = sum(person.is_vaccinated and person.infection is None for person in self.population)
		return saved

if __name__ == "__main__":
	# Test your simulation here
	virus = Virus("HIV", 0.8, 0.3)
	sim = Simulation(virus, 100000, 0.45, 10)
	sim.run()