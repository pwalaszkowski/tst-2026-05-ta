from selenium.webdriver.common.by import By

class PageObjects:
    name_field_locator = (By.ID, "name")
    salary_field_locator = (By.CSS_SELECTOR, "#salary")
    age_field_locator = (By.XPATH, "//*[@id='age']")