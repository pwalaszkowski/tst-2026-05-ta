import json
import logging
import pytest
import requests

BASE_URL = "http://localhost:8000"
HEALTH_CHECK = BASE_URL + "/health"
EMPLOYEES = BASE_URL + "/api/employees"

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

def test_health_status(logger):
    logger.info("Start test_health_status test")
    payload = {}
    headers = {}

    response = requests.request("GET", HEALTH_CHECK, headers=headers, data=payload)
    assert response.text == '{"status":"ok"}', "Result is different than expected"
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 5.0

    body = response.json()
    assert body["status"] == "ok"

    logger.info("End test_health_status test")

# TODO: Napisz test, który sprawdzi sytuacje gdy adres jest niepoprawny

def test_create_new_employee(logger):

    # json.dump
    # json.dumps
    # json.load
    # json.loads

    payload = json.dumps({
        "name": "Jan Kowalski",
        "salary": 8000,
        "age": 30,
        "position": "Mid QA",
        "on_leave": False
    }) 
    # Shift + TAB

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", EMPLOYEES, headers=headers, data=payload)
    assert response.status_code == 200

    body = response.json()
    expected = {"name": "Jan Kowalski",
        "salary": 8000,
        "age": 30,
        "position": "Mid QA",
        "on_leave": False
        }
    
    for key, value in expected.items():
        logger.info(f"expected: {key}:{value}, got {body[key]}")
        assert body[key] == value, f"expected {key}:{value}, got:{body[key]}"
    
    #   pm.expect(json.name).to.be.a("string");
    logger.info(f"Expected type str is: {isinstance(body["name"], str)}")
    assert isinstance(body["name"], str)
    assert isinstance(body["age"], int)

    # isinstance(obiekt, oczekiwany typ danych)
    # int, str, bool, 

    global employee_id 
    employee_id = str(body["id"])
    logger.info(f"Employee ID: {employee_id}")
    # const json = pm.response.json();
    # pm.collectionVariables.set('employee_id', json.id);

   
def test_update_created_employee(logger):
    payload = json.dumps({
        "name": "Jan Kowalski",
        "salary": 10000,
        "age": 31,
        "position": "Senior QA",
        "on_leave": False
    }) 

    headers = {
        'Content-Type': 'application/json'
    }

    EMPLOYEE_TO_CHANGE = EMPLOYEES + "/" + employee_id
    logger.info(f"Changed employee: {employee_id}")
    response = requests.request("PUT", EMPLOYEE_TO_CHANGE, headers=headers, data=payload)
    assert response.status_code == 200

    # TODO: Dopisz asercje ktore sprawdza czy pracownik zostal zmieniony (na podstawie metody POST)

def test_delete_created_employee(logger):
    EMPLOYEE_TO_CHANGE = EMPLOYEES + "/" + employee_id
    logger.info(f"Deleted employee: {employee_id}")
    response = requests.request("DELETE", EMPLOYEE_TO_CHANGE)
    assert response.status_code == 200

    response = requests.request("GET", EMPLOYEES)
    body = response.json()
    logger.info(body)
    ids = [emp["id"] for emp in body]
    assert int(employee_id) not in ids, f"Employee {employee_id} still present after delete: {body}"

@pytest.mark.skip(reason="This is not implemented yet")
def test_placeholder():
    pass

def test_placeholder_inside():
    # Wyszukujemy loty na 30 dni w przod EPGD - EPWA 
    flights = 0 
    if flights == 0:
        pytest.skip("We cannot find any flights for next 30 days")