# -*- encoding: utf-8 -*-
"""
@Author : hebe_tian
"""
from selenium import webdriver


class TestPages:

    def test_page_movies(self):
        driver = webdriver.Chrome()
        driver.get('http://diudiu.pythonanywhere.com/')
        driver.find_element_by_xpath('/html/body/nav/ul/li[1]/a').click()
        text = driver.find_element_by_xpath('/html/body/p').text
        assert 'Movies' in text
        driver.quit()

    def test_page_books(self):
        driver = webdriver.Chrome()
        driver.get('http://diudiu.pythonanywhere.com/')
        driver.find_element_by_xpath('/html/body/nav/ul/li[2]/a').click()
        text = driver.find_element_by_xpath('/html/body/p').text
        assert 'Books' in text
        driver.quit()

    def test_page_login(self):
        driver = webdriver.Chrome()
        driver.get('http://diudiu.pythonanywhere.com/')
        driver.find_element_by_xpath('/html/body/nav/ul/li[3]/a').click()
        text = driver.find_element_by_xpath('/html/body/h3').text
        assert text == 'Login'

    def test_page_about_me(self):
        driver = webdriver.Chrome()
        driver.get('http://diudiu.pythonanywhere.com/')
        driver.find_element_by_xpath('/html/body/nav/ul/li[4]/a').click()
        text = driver.find_element_by_xpath('/html/body/h2[2]').text
        assert 'DiuDiu' == text
