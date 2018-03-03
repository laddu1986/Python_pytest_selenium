from selenium import webdriver


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

    def destroy(self):
        self.wd.quit()
