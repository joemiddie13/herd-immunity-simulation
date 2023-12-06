class Virus(object):
	"""
	This class represents a virus in the simulation. 
	Each virus has a name, a reproductive rate, and a mortality rate.
	"""
	def __init__(self, name, repro_rate, mortality_rate):
		"""
		Initialize a new instance of the virus.
		Args:
				name (str): The name of the virus.
				repro_rate (float): The reproductive rate of the virus, representing how infectious it is.
				mortality_rate (float): The mortality rate of the virus, representing how deadly it is.
		"""
		if repro_rate < 0 or repro_rate > 1:
				raise ValueError("Invalid reproductive rate. It must be between 0 and 1.")
		if mortality_rate < 0 or mortality_rate > 1:
				raise ValueError("Invalid mortality rate. It must be between 0 and 1.")

		self.name = name
		self.repro_rate = repro_rate
		self.mortality_rate = mortality_rate

if __name__ == "__main__":
	# Test 1: Verify attributes of the HIV virus
	hiv_virus = Virus("HIV", 0.8, 0.3)
	assert hiv_virus.name == "HIV"
	assert hiv_virus.repro_rate == 0.8
	assert hiv_virus.mortality_rate == 0.3
	print("HIV virus tests passed successfully.")

	# Test 2: Verify attributes of a different virus, e.g., Influenza
	flu_virus = Virus("Influenza", 0.5, 0.1)
	assert flu_virus.name == "Influenza"
	assert flu_virus.repro_rate == 0.5
	assert flu_virus.mortality_rate == 0.1
	print("Influenza virus tests passed successfully.")

	# Test 3: Check handling of invalid reproductive rate
	try:
			invalid_virus = Virus("InvalidVirus", -0.5, 0.3)
			assert False, "Creation of virus with invalid reproductive rate did not raise error."
	except ValueError as e:
			print("Invalid reproductive rate test passed successfully: " + str(e))

	# Test 4: Check handling of invalid mortality rate
	try:
			invalid_virus = Virus("InvalidVirus", 0.5, 1.1)
			assert False, "Creation of virus with invalid mortality rate did not raise error."
	except ValueError as e:
			print("Invalid mortality rate test passed successfully: " + str(e))