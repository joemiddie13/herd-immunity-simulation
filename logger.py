import datetime

class Logger(object):
	def __init__(self, file_name):
		self.file_name = file_name

	def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
		date_of_simulation = datetime.datetime.now().strftime("%Y-%m-%d")
		with open(self.file_name, 'w') as file:
			file.write(f"Population Size: {pop_size}\n")
			file.write(f"Vaccination Percentage: {vacc_percentage}\n")
			file.write(f"Virus Name: {virus_name}\n")
			file.write(f"Mortality Rate: {mortality_rate}\n")
			file.write(f"Basic Reproduction Number: {basic_repro_num}\n")
			file.write(f"Date of Simulation: {date_of_simulation}\n\n")

	def log_time_step(self, step_number, new_infections, new_deaths, current_population, total_deaths, total_vaccinated):
		with open(self.file_name, 'a') as file:
				file.write("----------------------------\n")
				file.write(f"Time Step Number: {step_number}\n")
				file.write("----------------------------\n\n")
				file.write(f"Number of New Infections: {new_infections}\n")
				file.write(f"Number of New Deaths: {new_deaths}\n\n")
				file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
				file.write(f"Current Population Count: {current_population}\n")
				file.write(f"Total Number of Deaths: {total_deaths}\n")
				file.write(f"Total Number of Vaccinations Administered: {total_vaccinated}\n\n")

	def write_final_summary(self, survivors, total_deaths, total_vaccinated, reason, total_interactions, newly_vaccinated, infected_percentage, death_percentage, lives_saved):
		with open(self.file_name, 'a') as file:
				file.write("-~-~-~-~-~-~-~-~-~-~-~-~-~-\n\n")
				file.write(f"Number of Survivors: {survivors}\n")
				file.write(f"Total Number of Deaths: {total_deaths}\n")
				file.write(f"Total Number of Vaccinations: {total_vaccinated}\n")
				file.write(f"Reason for Simulation Ending: {reason}\n")
				file.write(f"Total Number of Interactions: {total_interactions}\n")
				file.write(f"Newly Vaccinated Count: {newly_vaccinated}\n")
				file.write(f"Percentage of Population That Became Infected: {infected_percentage}%\n")
				file.write(f"Percentage of Population That Died: {death_percentage}%\n")
				file.write(f"Number of Lives Saved by Vaccinations: {lives_saved}\n")