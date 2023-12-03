class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of your virus
        # TODO Define the other attributes of Virus
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


# Test this class (original from assignment)
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3
    # Test passes!

    # Additional test #1
    virus = Virus("Tuberculosis", 0.5, 0.8)
    assert virus.name == "Tuberculosis"
    assert virus.repro_rate == 0.5 
    assert virus.mortality_rate == 0.8

    #Additional test #2
    virus = Virus("Salmonella", 0.9, 0.3)
    assert virus.name == "Salmonella"
    assert virus.repro_rate == 0.9 
    assert virus.mortality_rate == 0.3