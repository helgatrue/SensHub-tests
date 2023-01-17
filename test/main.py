from selenium import webdriver
from locators import LogIn, Dashboard
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logs.logs import log_config
from selenium.webdriver.common.keys import Keys
import config
from test.util import get_dated_name


@log_config
def send_letter_test():
    driver = webdriver.Chrome('chromedriver')
    driver.maximize_window()
    driver.get("https://st-dev.scrdairy.com/")
    driver.find_element(*LogIn.USER_NAME).send_keys(config.username)
    driver.find_element(*LogIn.PASSWORD).send_keys(config.password)
    driver.find_element(*LogIn.FARM_ID).send_keys(config.id)
    driver.find_element(*LogIn.SUBMIT_BTN).click()

    timeout = 5
    try:
        element_present = EC.url_contains('https://st-dev.scrdairy.com/6.3.2.225/')
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page https://st-dev.scrdairy.com/6.3.2.225/ is loaded")

    timeout = 25
    try:
        element_present = EC.url_contains('https://st-dev.scrdairy.com/6.3.2.225/#/dashboard')
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page https://st-dev.scrdairy.com/6.3.2.225/#/dashboard is loaded")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((Dashboard.SEARCH_BTN)))
    driver.find_element(*Dashboard.SEARCH_BTN).click()
    driver.find_element(*Dashboard.SEARCH_FIELD).send_keys("0004", Keys.ENTER)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((Dashboard.MENU_HEAT)))
    driver.find_element(*Dashboard.MENU_HEAT).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((Dashboard.HEAT_DASHBOARD)))
    driver.get_screenshot_as_file(get_dated_name('screenshots/heat-', '.png'))
    driver.close()


if __name__ == '__main__':
    send_letter_test()
