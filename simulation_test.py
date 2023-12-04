from simulation import Simulation
from virus import Virus

def test_initialization():
    virus = Virus("TestVirus", 0.5, 0.2)
    simulation = Simulation(virus, 100, 0.1, 5)
    assert simulation.pop_size == 100
    assert simulation.vacc_percentage == 0.1
    assert len(simulation.population) == 100

def test_population_creation():
    virus = Virus("TestVirus", 0.5, 0.2)
    simulation = Simulation(virus, 100, 0.2, 5)
    vaccinated_count = sum(p.is_vaccinated for p in simulation.population)
    infected_count = sum(p.infection == virus for p in simulation.population)
    assert vaccinated_count == 20
    assert infected_count == 5

def test_simulation_step():
    virus = Virus("TestVirus", 0.5, 0.2)
    simulation = Simulation(virus, 10, 0.2, 1)
    simulation.time_step()

def test_simulation_completion():
    virus = Virus("TestVirus", 0.5, 0.2)
    simulation = Simulation(virus, 10, 1, 0)  # All vaccinated, no infected
    steps = simulation.run()
    assert steps == 1

# Run tests
test_initialization()
test_population_creation()
test_simulation_step()
test_simulation_completion()
