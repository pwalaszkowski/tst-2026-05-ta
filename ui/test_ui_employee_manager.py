import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

BASE_UI_URL = "http://localhost:8000/"

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    # options.add_experimental_option()

    driver = webdriver.Chrome(options=options)
    # Options - 
    # - rozdzielczosc -> RWD -> responsive web design 
    # - headless - 
    # - disable alerts 
    # - experimental options  
    # - incognito mode 
    driver.implicitly_wait(5)
    driver.get(BASE_UI_URL)
    yield driver
    driver.quit()
    

def test_check_title(driver):
    assert driver.title == "Employee Manager", "Title is different"

def test_add_new_employee(driver):
    name_textfield = driver.find_element(By.ID, "name")
    name_textfield.send_keys("Jan Kowalski")
    name_value = name_textfield.get_attribute("value")
    assert name_value == "Jan Kowalski"

    sleep(1)

    # driver.find_element(By.CLASS_NAME)
    salary_textfield = driver.find_element(By.CSS_SELECTOR, "#salary")
    salary_textfield.send_keys("10000")
    salary_value = salary_textfield.get_attribute("value")
    assert salary_value == "10000"

    sleep(1)

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
    sleep(1)

    vacation_checkbox = driver.find_element(By.ID, "on_leave")
    vacation_value = vacation_checkbox.is_selected()
    assert vacation_value is False

    add_button = driver.find_element(By.CLASS_NAME, "btn-add")
    # Sprawdzamy czy przycisk jest widoczny dla naszych oczu
    assert add_button.is_displayed()
    # Sprawdzamy czy jest enabled (czy mozemy kliknac)
    assert add_button.is_enabled()
    
    add_button.click()
    
    driver.save_screenshot("screenshot_name.png")

    sleep(5)
    
    # driver.find_element(By.LINK_TEXT, "Codebrainers")
    # driver.find_element(By.PARTIAL_LINK_TEXT, "Code")
    # driver.find_element(By.NAME)
    # driver.find_element(By.TAG_NAME)
    # driver.find_elements
    # <input id="name" maxlength="50" placeholder="Name" style="">
    # implicit
    # explicit

# TODO:
# Explicit wait
# Tabelka - jak weryfikac dane w tabeli
# Page Object Model/Page Object Pattern 
# 