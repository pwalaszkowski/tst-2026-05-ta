import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


def test_check_title(driver):
    assert driver.title == "Employee Manager", "Title is different"

def test_add_new_employee(driver):
    name_textfield = driver.find_element(By.ID, "name")
    name_textfield.send_keys("Jan Kowalski")
    name_value = name_textfield.get_attribute("value")
    assert name_value == "Jan Kowalski"

    # driver.find_element(By.CLASS_NAME)
    salary_textfield = driver.find_element(By.CSS_SELECTOR, "#salary")
    salary_textfield.send_keys("10000")
    salary_value = salary_textfield.get_attribute("value")
    assert salary_value == "10000"

    age_textfield = driver.find_element(By.XPATH, "//*[@id='age']")
    # age_textfield = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/input[3]")
    age_textfield.send_keys("32")
    age_value = age_textfield.get_attribute("value")
    assert age_value == "32"
    
    position_dropdown = Select(driver.find_element(By.ID, "position"))
    # ["Junior QA", "Mid QA", "Senior QA", "QA Lead"]
    # position_dropdown.select_by_value("Junior QA")
    # position_dropdown.select_by_index()
    position_dropdown.select_by_visible_text("Junior QA")
    selected_option = position_dropdown.first_selected_option
    position_value = selected_option.get_attribute("value")
    assert position_value == "Junior QA"

    vacation_checkbox = driver.find_element(By.ID, "on_leave")
    vacation_value = vacation_checkbox.is_selected()
    assert vacation_value is False

    WAIT = WebDriverWait(driver, 10)
    add_button = WAIT.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-add")))
    # (By.CLASS_NAME, "btn-add")
    add_button.click()

    # EC.presence_of_element_located  # czekamy na obiekt z kodu html/dom 
    # EC.visibility_of_element_located    # czekamy az obiekt/element bedzie widoczny golym okiem
    # EC.element_to_be_clickable  # mozna to klikanc
    # EC.text_to_be_present_in_element    # czekamy na konkretny tekst ktory jest widoczny
    # add_button = driver.find_element(By.CLASS_NAME, "btn-add")
    # Sprawdzamy czy przycisk jest widoczny dla naszych oczu
    # assert add_button.is_displayed()
    # Sprawdzamy czy jest enabled (czy mozemy kliknac)
    # assert add_button.is_enabled()    
    # add_button.click()
    
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
    
    # driver.find_element(By.LINK_TEXT, "Codebrainers")
    # driver.find_element(By.PARTIAL_LINK_TEXT, "Code")
    # driver.find_element(By.NAME)
    # driver.find_element(By.TAG_NAME)
    # driver.find_elements
    # <input id="name" maxlength="50" placeholder="Name" style="">
    # implicit
    # explicit

# Page Object Model/Page Object Pattern  