import pytest
import pytest_html.extras
from selenium import webdriver

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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            screenshot = driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, name="screenshot"))

    report.extra = extra
