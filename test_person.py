# Test an infected person who is not vaccinated
infected_person = Person(4, False, virus)
assert infected_person._id == 4
assert infected_person.is_vaccinated is False
assert infected_person.infection == virus# Test an infected person who is not vaccinated
infected_person = Person(4, False, virus)
assert infected_person._id == 4
assert infected_person.is_vaccinated is False
assert infected_person.infection == virus

# Test the survival of an infected person
survived = infected_person.did_survive_infection()
assert survived is False  # Since the mortality rate of the virus is 0.2

# Test the updated attributes of the infected person
assert infected_person.is_alive is False
assert infected_person.is_vaccinated is False
assert infected_person.infection is None