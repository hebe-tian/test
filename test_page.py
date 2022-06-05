# -*- encoding: utf-8 -*-
"""
@Author : hebe_tian
"""
import pytest
from selenium import webdriver
import json


with open("data.json", 'r', encoding='utf-8') as f:
    data = json.load(f)
    url = data['url']

    xpath = data['page']
    movie_path = xpath['movie_path']
    book_path = xpath['book_path']
    movie_text_path = xpath['assert_text_path']
    book_text_path = xpath['assert_text_path']
    login_path = xpath['login_path']
    login_text_path = xpath['login_text_path']
    about_me_path = xpath['about_me_path']
    about_me_text_path = xpath['about_me_text_path']

    username_path = xpath['username_path']
    password_path = xpath['password_path']
    login_submit_path = xpath['login_submit_path']
    alert_path = xpath['alert_path']
    logout_path = xpath['logout_path']
    settings_path = xpath['settings_path']
    settings_text_path = xpath['settings_text_path']
    f.close()

with open("userdata.json", 'r', encoding='utf-8') as f:
    data = json.load(f)
    name = data['username']
    password = data['password']
    f.close()


@pytest.mark.skip()
class TestPages:

    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)

    def test_page_movies(self):
        self.driver.find_element_by_xpath(movie_path).click()
        text = self.driver.find_element_by_xpath(movie_text_path).text
        assert 'Movies' in text

    def test_page_books(self):
        self.driver.find_element_by_xpath(book_path).click()
        text = self.driver.find_element_by_xpath(book_text_path).text
        assert 'Books' in text

    def test_page_login(self):
        self.driver.find_element_by_xpath(login_path).click()
        text = self.driver.find_element_by_xpath(login_text_path).text
        assert text == 'Login'

    def test_page_about_me(self):
        self.driver.find_element_by_xpath(about_me_path).click()
        text = self.driver.find_element_by_xpath(about_me_text_path).text
        assert 'DiuDiu' == text

    def teardown(self):
        self.driver.quit()


@pytest.mark.skip()
class TestLogin:

    def setup(self):
        """open chrome and get url"""
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url+'/login')

    def test_login_without_all(self):
        self.driver.find_element_by_xpath(login_submit_path).click()
        text = self.driver.find_element_by_xpath(login_text_path).text
        assert 'Login' in text

    def test_login_wrong_msg(self):
        self.driver.find_element_by_xpath(username_path).send_keys(name)
        self.driver.find_element_by_xpath(password_path).send_keys('password')
        self.driver.find_element_by_xpath(login_submit_path).click()
        text = self.driver.find_element_by_xpath(alert_path).text
        assert 'Invalid' in text

    def test_login_right_msg(self):
        self.driver.find_element_by_xpath(username_path).send_keys(name)
        self.driver.find_element_by_xpath(password_path).send_keys(password)
        self.driver.find_element_by_xpath(login_submit_path).click()
        text = self.driver.find_element_by_xpath(alert_path).text
        assert 'success' in text

    def teardown(self):
        self.driver.quit()


class TestUser:

    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url+'/login')

    def login(self):
        self.driver.find_element_by_xpath(username_path).send_keys(name)
        self.driver.find_element_by_xpath(password_path).send_keys(password)
        self.driver.find_element_by_xpath(login_submit_path).click()

    def test_not_login(self):
        text = self.driver.find_element_by_xpath(logout_path).text
        assert text != 'Logout'

    def test_login(self):
        self.login()
        text = self.driver.find_element_by_xpath(logout_path).text
        assert text == 'Logout'

    def test_login_settings(self):
        self.login()
        self.driver.find_element_by_xpath(settings_path).click()
        text = self.driver.find_element_by_xpath(settings_text_path).text
        assert text == 'Settings'

    def test_logout(self):
        self.login()
        self.driver.find_element_by_xpath(logout_path).click()
        text = self.driver.find_element_by_xpath(alert_path).text
        assert text == 'Goodbye.'

    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(["--html", "./reports/report.html"])
