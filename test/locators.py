from selenium.webdriver.common.by import By


class LogIn:
    USER_NAME = (By.XPATH, '//input[@name="username"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    FARM_ID = (By.XPATH, '//input[@name="farmId"]')
    SUBMIT_BTN = (By.XPATH, '//input[@type="submit"]')


class Dashboard:
    SEARCH_BTN = (By.XPATH, '//*[@sh-id="header_search_toggleSearch"]')
    SEARCH_FIELD = (By.XPATH, '//*[@sh-id="header_search_searchTerm"]')
    MENU_HEAT = (By.XPATH, '//*[text()="Heat"]')
    HEAT_DASHBOARD = (By.CSS_SELECTOR, "#chart-container_ChartAreaBorder")
