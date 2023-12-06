import random
from virus import Virus

class Person(object):
  """
  This class represents a person in the simulation. Each person has an ID, a vaccination
  status, and potentially an infection.
  """
  def __init__(self, _id, is_vaccinated, infection=None):
    """
    Initialize a new person.
    Args:
      _id (int): The unique identifier for the person.
      is_vaccinated (bool): Indicates whether the person is vaccinated.
      infection (Virus, optional): The virus this person is infected with, if any.
    """
    self._id = _id
    self.is_vaccinated = is_vaccinated
    self.infection = infection
    self.is_alive = True  # Initially, every person is alive.

  def did_survive_infection(self):
    """
    Determines if an infected person survives their infection.
    Returns:
      bool: True if the person survives the infection, False otherwise, None if not infected.
    """
    if self.infection:
      survival_chance = random.random()
      if survival_chance < self.infection.mortality_rate:
        self.is_alive = False
        return False
      else:
        self.is_vaccinated = True
        self.infection = None
        return True
    else:
      return None

if __name__ == "__main__":
  # Test cases for the Person class

  # Testing a vaccinated person
  vaccinated_person = Person(1, True)
  print("Testing a vaccinated person...")
  print(f"ID: {vaccinated_person._id}, Vaccinated: {vaccinated_person.is_vaccinated}, Infection: {vaccinated_person.infection}")
  
  # Testing an unvaccinated person
  unvaccinated_person = Person(2, False)
  print("\nTesting an unvaccinated person...")
  print(f"ID: {unvaccinated_person._id}, Vaccinated: {unvaccinated_person.is_vaccinated}, Infection: {unvaccinated_person.infection}")

  # Testing an infected person
  virus = Virus("Dysentery", 0.7, 0.2)
  infected_person = Person(3, False, virus)
  print("\nTesting an infected person...")
  print(f"ID: {infected_person._id}, Vaccinated: {infected_person.is_vaccinated}, Infection: {infected_person.infection.name}")

  # Testing survival rate for infected people
  people = [Person(i, False, virus) for i in range(1, 101)]
  did_survive = 0
  did_not_survive = 0
  print("\nTesting survival rate for infected people...")
  for person in people:
    survived = person.did_survive_infection()
    if survived:
      did_survive += 1
    elif survived is False:
      did_not_survive += 1
  print(f"Survived: {did_survive}, Did Not Survive: {did_not_survive}")

  # Stretch challenge: Testing infection rate among uninfected people
  uninfected_people = [Person(i + 100, False) for i in range(1, 101)]
  infected_count = 0
  print("\nTesting infection rate among uninfected people...")
  for person in uninfected_people:
    if random.random() < virus.repro_rate:
      person.infection = virus
      infected_count += 1
  print(f"Infected Count: {infected_count}, Total: {len(uninfected_people)}")