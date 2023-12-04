import os
from logger import Logger

def test_write_metadata():
    logger = Logger("test_log.txt")
    logger.write_metadata(100, 0.2, "TestVirus", 0.05, 1.0)
    with open("test_log.txt", "r") as file:
        contents = file.read()
        assert "Population size: 100" in contents
        assert "Vaccination Percentage: 0.2" in contents

def test_log_interactions():
    logger = Logger("test_log.txt")
    logger.log_interactions(1, 50, 5)
    with open("test_log.txt", "r") as file:
        contents = file.read()
        assert "Step 1: Interactions: 50, New Infections: 5" in contents

def test_log_infection_survival():
    logger = Logger("test_log.txt")
    logger.log_infection_survival(1, 95, 5)
    with open("test_log.txt", "r") as file:
        contents = file.read()
        assert "Step 1: Population Count: 95, New Fatalities: 5" in contents

def test_log_time_step():
    logger = Logger("test_log.txt")
    logger.log_time_step(1)
    with open("test_log.txt", "r") as file:
        contents = file.read()
        assert "End of Step 1" in contents

test_write_metadata()
test_log_interactions()
test_log_infection_survival()
test_log_time_step()