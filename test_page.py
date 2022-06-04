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


if __name__ == '__main__':
    pytest.main(["--html", "./reports/report.html"])
