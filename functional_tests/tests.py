from selenium import webdriver
import unittest
import time

class HomeText(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_display_hello_world_in_index(self):
        # 打开应用的首页，应显示：Hello, world. You're at mysite index.
        self.browser.get('http://127.0.0.1:8000')

        body_text = self.browser.find_element_by_tag_name('body').text

        self.assertIn("Hello, world. You're at mysite index.", body_text)

    if __name__ == '__main__':
        unittest.main(warnings='ignore')
