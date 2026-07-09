from page_objects import PageObjects

def enter_name(driver, text):
    name = driver.find_element(*PageObjects.name_field_locator)
    name.send_keys(text)
    name_value = name.get_attribute("value")
    assert name_value == text

def enter_salary(driver, salary_text):
    salary = driver.find_element(*PageObjects.salary_field_locator)
    salary.send_keys(salary_text)
    salary_value = salary.get_attribute("value")
    assert salary_value == salary_text

def enter_age(driver, age_text):
    age = driver.find_element(*PageObjects.age_field_locator)
    age.send_keys("32")
    age_value = age.get_attribute("value")
    assert age_value == age_text