import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.logger = Logger("simulation_log.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        # TODO: Store the virus in an attribute
        # TODO: Store pop_size in an attribute
        # TODO: Store the vacc_percentage in a variable
        # TODO: Store initial_infected in a variable
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not. 
        # Use the _create_population() method to create the list and 
        # return it storing it in an attribute here. 
        # TODO: Call self._create_population() and pass in the correct parameters.
        self.population = self._create_population()
        self.current_step = 0
        self.newly_infected = []

    def _create_population(self):
        population = []
        num_vaccinated = int(self.pop_size * self.vacc_percentage)
        num_infected = self.initial_infected

        for i in range(self.pop_size):
            is_vaccinated = False
            infection = None

            if num_vaccinated > 0:
                is_vaccinated = True
                num_vaccinated -= 1
            elif num_infected > 0:
                infection = self.virus
                num_infected -= 1

            new_person = Person(i, is_vaccinated, infection)
            population.append(new_person)

        random.shuffle(population)
        return population

    def _simulation_should_continue(self):
        # This method will return a boolean indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        # TODO: Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.
        living_people = 0
        vaccinated_people = 0

        for person in self.population:
            if person.is_alive:
                living_people += 1
                if person.is_vaccinated:
                    vaccinated_people += 1
        
        if living_people == 0:
            return False
        
        if living_people == vaccinated_people:
            return False
        
        return True

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step.

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name,
                                   self.virus.mortality_rate, self.virus.repro_rate) 

        time_step_counter = 0
        should_continue = True

        while should_continue:
            # TODO: Increment the time_step_counter
            # TODO: for every iteration of this loop, call self.time_step() 
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            time_step_counter += 1
            self.time_step()
            should_continue = self._simulation_should_continue()
            
            return time_step_counter

        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        new_infections = []
        interaction_count = 0

        for person in self.population:
            if person.is_alive and person.infection:
                for _ in range(100):
                    random_person = random.choice(self.population)
                    while random_person == person:
                        random_person = random.choice(self.population)
                    
                    self.interaction(person, random_person, new_infections)
        
        self._infect_newly_infected()
        self.logger.log_interactions(self.current_step, interaction_count, len(new_infections))

    def interaction(self, infected_person, random_person, new_infections):
        # TODO: Finish this method.
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.
        
        if not random_person.is_vaccinated and random_person.infection is None:
            if random.random() < self.virus.repro_rate:
                new_infections.append(random_person)
                
                self.logger.log_interactions(infected_person, random_person, "New Infection")
            else:
                self.logger.log_interactions(infected_person, random_person, "No Infection")
        
        

    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for person in self.newly_infected:
            if person.is_alive and not person.is_vaccinated:
                person.infection = self.virus
        
        self.newly_infected = []


if __name__ == "__main__":
    # Define the virus characteristics
    virus_name = "Sniffles"
    repro_num = 0.5  # Reproduction number
    mortality_rate = 0.12  # Mortality rate

    # Create a Virus instance
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Create an instance of the Simulation
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()