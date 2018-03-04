from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Application:

    def __init__(self, browser, pub_url, priv_url, user, password):
        if browser.lower() == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser.lower() == 'ie':
            self.wd = webdriver.Ie()
        elif browser.lower() == 'safari':
            self.wd = webdriver.Safari()
        else:
            raise ValueError('Unrecognized browser "%s"' % browser)
        self.pub_url = pub_url
        self.priv_url = priv_url
        self.user = user
        self.password = password
        self.chat_compare_relative_url = 'chat/compare/#compare'

    def destroy(self):
        self.wd.quit()

    def wait_for_element_to_be_visible(self, selector):
        WebDriverWait(self.wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def navigate_to(self, url):
        self.wd.get(url)

    def navigate_to_chat_compare_page(self):
        self.navigate_to(self.pub_url + self.chat_compare_relative_url)
        self.wait_for_element_to_be_visible('.compare-table')  # wait for comparison table to be loaded
