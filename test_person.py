# Test an infected person who is not vaccinated
infected_person = Person(4, False, virus)
assert infected_person._id == 4
assert infected_person.is_vaccinated is False
assert infected_person.infection == virus