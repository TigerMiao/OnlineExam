from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import home_page
from .models import Question

class HomePageTest(TestCase):

    def test_home_page_return_correct_html(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'onlineexam/home.html')

class QuestionModelTest(TestCase):

    def test_save_and_retrieving_questions(self):
        first_question = Question()
        first_question.text = 'The first question'
        first_question.save()

        second_question = Question()
        second_question.text = 'The second question'
        second_question.save()

        saved_questions = Question.objects.all()
        self.assertEqual(saved_questions.count(), 2)

        first_saved_question = saved_questions[0]
        second_saved_question = saved_questions[1]
        self.assertEqual(first_saved_question.text, 'The first question')
        self.assertEqual(second_saved_question.text, 'The second question')
