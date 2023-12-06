import unittest
from simulation import Simulation
from virus import Virus
from person import Person

class SimulationTest(unittest.TestCase):
	"""
	This class contains unit tests for the Simulation class.
	"""

	def setUp(self):
		"""
		Set up a simulation instance with a test virus and population.
		"""
		virus = Virus("TestVirus", 0.2, 0.6)
		self.simulation = Simulation(virus, 100, 0.2, 10)

	def test_create_population(self):
		"""
		Test the creation of a population with the correct number of vaccinated and infected individuals.
		"""
		self.assertEqual(len(self.simulation.population), 100)
		vaccinated_count = sum(person.is_vaccinated for person in self.simulation.population)
		infected_count = sum(person.infection is not None for person in self.simulation.population)
		self.assertEqual(vaccinated_count, 20)
		self.assertEqual(infected_count, 10)

	def test_simulation_should_continue(self):
		"""
		Test if the simulation should continue based on the current state of the population.
		"""
		continue_simulation = self.simulation._simulation_should_continue()
		self.assertTrue(continue_simulation)

	def test_interaction(self):
		"""
		Test interactions between an infected person and a healthy person.
		"""
		infected_person = Person(1, False, self.simulation.virus)
		healthy_person = Person(2, False)
		interaction_result = self.simulation.interaction(infected_person, healthy_person)
		self.assertIsInstance(interaction_result, bool)

	def test_time_step(self):
		"""
		Test the simulation time step for increasing the number of infected individuals.
		"""
		self.simulation.time_step()

if __name__ == '__main__':
	unittest.main()
