# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestLoginSuccess():
    def setup_method(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_loginSuccess(self):
        self.driver.get("http://demo.guru99.com/test/newtours/login.php")
        self.driver.set_window_size(1920, 982)
        self.driver.find_element(By.NAME, "userName").click()
        self.driver.find_element(By.NAME, "userName").send_keys("user")
        self.driver.find_element(By.NAME, "password").send_keys("pass")
        self.driver.find_element(By.NAME, "submit").click()
        assert "Login Successfully" == self.driver.find_element(
            By.CSS_SELECTOR, "h3").text

    def test_wrong(self):
      self.driver.get("http://demo.guru99.com/test/newtours/login.php")
      self.driver.set_window_size(974, 1047)
      self.driver.find_element(By.NAME, "userName").click()
      self.driver.find_element(By.NAME, "userName").send_keys("my_user")
      self.driver.find_element(By.NAME, "password").click()
      self.driver.find_element(By.NAME, "password").send_keys("my_pass")
      self.driver.find_element(By.NAME, "submit").click()
      assert "Enter your userName and password correct" == self.driver.find_element(By.CSS_SELECTOR, "span").text


def main():
    test = TestLoginSuccess()
    test.setup_method()
    test.test_loginSuccess()
    test.test_wrong()
    test.teardown_method()
    print("final")

main()
