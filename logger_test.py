import unittest
import os
from logger import Logger

class LoggerTest(unittest.TestCase):
	"""
	This class contains unit tests for the Logger class.
	"""

	def setUp(self):
		"""
		Set up a logger instance with a test file name.
		"""
		self.filename = 'test_log.txt'
		self.logger = Logger(self.filename)

	def test_write_metadata(self):
		"""
		Test writing metadata to the log file.
		"""
		self.logger.write_metadata(100, 0.2, "TestVirus", 0.05, 1.0)
		with open(self.filename, 'r') as file:
				data = file.readlines()
		self.assertTrue("Population Size: 100" in data[0])
		self.assertTrue("Virus Name: TestVirus" in data[2])

	def test_log_time_step(self):
		"""
		Test logging a time step.
		"""
		self.logger.write_metadata(100, 0.2, "TestVirus", 0.05, 1.0)
		self.logger.log_time_step(1, 10, 5, 95, 0, 20)
		with open(self.filename, 'r') as file:
				data = file.readlines()
		found_time_step_log = any("Time Step Number: 1" in line for line in data)
		self.assertTrue(found_time_step_log, "Time Step Number: 1 log entry not found in file.")

	def test_final_summary(self):
		"""
		Test writing the final summary of the simulation.
		"""
		self.logger.write_final_summary(95, 5, 20, "Simulation ended", 1000, 20, 10.0, 5.0, 15)
		with open(self.filename, 'r') as file:
				data = file.read()
		self.assertIn("Reason for Simulation Ending: Simulation ended", data)
		self.assertIn("Percentage of Population That Became Infected: 10.0%", data)

	def tearDown(self):
		"""
		Clean up by removing the test log file after tests are done.
		"""
		try:
				os.remove(self.filename)
		except FileNotFoundError:
				pass

if __name__ == '__main__':
	unittest.main()