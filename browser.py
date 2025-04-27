from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Browser():
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #     # Add headless option
    # options.add_argument('--headless')
    # options.add_argument('--window-size=2560x1440')
    s = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=s, options=options)
    wait = WebDriverWait(driver, 10)
    element = WebElement

    driver.implicitly_wait(20)
    driver.set_page_load_timeout(20)
    driver.maximize_window()
    driver.delete_all_cookies()

    def close(self):
        self.driver.close()
