from selenium import webdriver
from onlineexam.models import Question
import unittest
import time

class HomeText(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_display_first_question_in_home(self):
        # 打开应用的首页，title显示：Online Exam
        self.browser.get('http://127.0.0.1:8000')

        self.assertEqual('Online Exam', self.browser.title)

        # 首页应该显示第一个question
        question = self.browser.find_element_by_id('id_question_text')

        self.assertIn('1.', question.text)

    def test_next_button_in_home(self):
        self.browser.get('http://127.0.0.1:8000')

        # 首页应该显示第一个question
        question = self.browser.find_element_by_id('id_question_text')

        self.assertIn('1.', question.text)

        # 首页应该显示next按钮
        next = self.browser.find_element_by_id('id_next')
        next.click()

        # 点击next按钮后显示第二个question
        question = self.browser.find_element_by_id('id_question_text')

        self.assertIn('2.', question.text)

        # 首页应该显示last按钮
        last = self.browser.find_element_by_id('id_last')
        last.click()

        # 点击last按钮后显示第一个question
        question = self.browser.find_element_by_id('id_question_text')

        self.assertIn('1.', question.text)

    if __name__ == '__main__':
        unittest.main(warnings='ignore')
