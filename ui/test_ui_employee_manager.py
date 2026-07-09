from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

from page_methods import enter_name, enter_salary, enter_age

def test_check_title(driver):
    assert driver.title == "Employee Manager", "Title is different"

def test_add_new_employee(driver):
    enter_name(driver, "Jan Kowalski")
    enter_salary(driver, "10000")
    enter_age(driver, "32")

    position_dropdown = Select(driver.find_element(By.ID, "position"))
    position_dropdown.select_by_visible_text("Junior QA")
    selected_option = position_dropdown.first_selected_option
    position_value = selected_option.get_attribute("value")
    assert position_value == "Junior QA"

    vacation_checkbox = driver.find_element(By.ID, "on_leave")
    vacation_value = vacation_checkbox.is_selected()
    assert vacation_value is False

    WAIT = WebDriverWait(driver, 10)
    add_button = WAIT.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-add")))
    add_button.click()
    
    sleep(5)

    employee_table = driver.find_element(By.ID, "employees").text
    assert "Jan Kowalski" in employee_table

    table_cells = driver.find_elements(By.TAG_NAME, "td")
    assert table_cells[1].text == "Jan Kowalski"
    assert table_cells[2].text == "10000"

    last_row = driver.find_elements(By.CSS_SELECTOR, "#employees tr")[-1]
    cells = last_row.find_elements(By.TAG_NAME, "td")

    EXPECTED_HEADERS = ["ID", "Name", "Salary", "Age", "Position", "Vacation", "Actions"]

    assert len(cells) == len(EXPECTED_HEADERS)

    row = dict(zip(EXPECTED_HEADERS, [c.text for c in cells]))
    
    assert row["Name"] == "Jan Kowalski"
    assert row["Salary"] == "10000"
    assert row["Age"] == "32"
    assert row["Position"] == "Junior QA"
