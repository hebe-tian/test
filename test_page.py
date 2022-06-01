# -*- encoding: utf-8 -*-
"""
@Author : hebe_tian
"""
from selenium import webdriver


class TestPages:

    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get('http://diudiu.pythonanywhere.com/')

    def test_page_movies(self):
        self.driver.find_element_by_xpath('/html/body/nav/ul/li[1]/a').click()
        text = self.driver.find_element_by_xpath('/html/body/p').text
        assert 'Movies' in text

    def test_page_books(self):
        self.driver.find_element_by_xpath('/html/body/nav/ul/li[2]/a').click()
        text = self.driver.find_element_by_xpath('/html/body/p').text
        assert 'Books' in text

    def test_page_login(self):
        self.driver.find_element_by_xpath('/html/body/nav/ul/li[3]/a').click()
        text = self.driver.find_element_by_xpath('/html/body/h3').text
        assert text == 'Login'

    def test_page_about_me(self):
        self.driver.find_element_by_xpath('/html/body/nav/ul/li[4]/a').click()
        text = self.driver.find_element_by_xpath('/html/body/h2[2]').text
        assert 'DiuDiu' == text

    def teardown(self):
        self.driver.quit()
