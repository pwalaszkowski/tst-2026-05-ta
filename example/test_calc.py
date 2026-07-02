import logging
import pytest

# Kod kalkulatora
def add(a, b):
    return a + b
 
 
def subtract(a, b):
    return a - b
 
 
def multiply(a, b):
    return a * b
 
 
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Fixtures
@pytest.fixture
def prepare_data():
    return[5, 5]

@pytest.fixture
def logger():
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    # avoid adding duplicate handlers if fixture runs multiple times
    if not log.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
            datefmt="%H:%M:%S"
        ))
        log.addHandler(handler)

    log.info("Logger fixture initialized")
    return log

# TODO:
# Parametryzacja
# Testowania API przez requests

# Kod testów
@pytest.mark.codebrainers
def test_add(logger, prepare_data):
    logger.info("Test Started")
    logger.info(f"Data used for testing {prepare_data[0], prepare_data[1]}")
    assert add(prepare_data[0], prepare_data[1]) == 10, "Komunikat błędu"
    logger.debug("Debug Message")
    logger.error("Error Message")
    logger.warning("Warning Message")
    logger.info("Test Finished")

@pytest.mark.TEST_12345
def test_substract(prepare_data):
    assert subtract(prepare_data[0], prepare_data[1]) == 0 

@pytest.mark.parametrize("a, b, result",[
                        (2, 2, 4),
                        (1, 0, 1),
                        (3, 3, 9),
                        (5, 5, 25),
                        (10, 10, 100),
])
def test_multiply(a, b, result):
    assert multiply(a,b) == result


def test_divide(prepare_data):
    assert divide(prepare_data[0], prepare_data[1]) == 1.0
