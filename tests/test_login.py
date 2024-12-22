import unittest
from appium import webdriver
from time import sleep

class LoginTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "11",
            "deviceName": "emulator-5554",
            "app": "/path/to/your-app.apk",
            "automationName": "UiAutomator2"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        username_field = self.driver.find_element_by_accessibility_id("username")
        password_field = self.driver.find_element_by_accessibility_id("password")
        login_button = self.driver.find_element_by_accessibility_id("login_button")

        username_field.send_keys("testuser")
        password_field.send_keys("password123")
        login_button.click()

        sleep(3)
        dashboard = self.driver.find_element_by_accessibility_id("dashboard")
        self.assertIsNotNone(dashboard)

    def test_invalid_login(self):
        username_field = self.driver.find_element_by_accessibility_id("username")
        password_field = self.driver.find_element_by_accessibility_id("password")
        login_button = self.driver.find_element_by_accessibility_id("login_button")

        username_field.send_keys("wronguser")
        password_field.send_keys("wrongpassword")
        login_button.click()

        sleep(3)
        error_message = self.driver.find_element_by_accessibility_id("error_message")
        self.assertIsNotNone(error_message)

if __name__ == "__main__":
    unittest.main()
