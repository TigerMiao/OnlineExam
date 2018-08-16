from selenium import webdriver
from onlineexam.models import Question
import unittest
import time

class HomeText(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_display_hello_world_in_index(self):
        # 打开应用的首页，title显示：Online Exam
        self.browser.get('http://127.0.0.1:8000')

        self.assertEqual('Online Exam', self.browser.title)

        '''
        # 首页应该显示第一个question
        question_text = self.browser.find_element_by_id('id_question_text')
        first_question = Question.objects.first()

        self.assertEqual(Question.objects.count(), 2)

        self.assertEqual(first_question.text, question_text.text)
        '''

    if __name__ == '__main__':
        unittest.main(warnings='ignore')
