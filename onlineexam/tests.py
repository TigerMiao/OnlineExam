from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import home_page
from .models import Question, Answer

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

class QuestionAndAnswerViewTest(TestCase):
    def test_display_first_question(self):
        first_question = Question.objects.create(text='The first question')
        second_question = Question.objects.create(text='The second question')

        answerA = Answer.objects.create(text='The Answer A', question=first_question)
        answerB = Answer.objects.create(text='The Answer B', question=first_question)
        answerC = Answer.objects.create(text='The Answer C', question=first_question)
        answerD = Answer.objects.create(text='The Answer D', question=first_question)

        response = self.client.get('/')

        self.assertContains(response, '1. The first question')
        self.assertNotContains(response, '2. The second question')

        self.assertContains(response, 'The Answer A')
        self.assertContains(response, 'The Answer B')
        self.assertContains(response, 'The Answer C')
        self.assertContains(response, 'The Answer D')

class AnswerModelTest(TestCase):

    def test_save_and_retrieving_answer(self):
        question = Question.objects.create(text='The first question')

        answerA = Answer.objects.create(text='The Answer A', question=question)
        answerB = Answer.objects.create(text='The Answer B', question=question)
        answerC = Answer.objects.create(text='The Answer C', question=question)
        answerD = Answer.objects.create(text='The Answer D', question=question)

        saved_question = Question.objects.first()
        self.assertEqual(saved_question, question)

        saved_answers = Answer.objects.all()
        self.assertEqual(saved_answers.count(), 4)

        first_saved_answer = saved_answers[0]
        second_saved_answer = saved_answers[1]
        third_saved_answer = saved_answers[2]
        fourth_saved_answer = saved_answers[3]

        self.assertEqual(first_saved_answer.text, 'The Answer A')
        self.assertEqual(first_saved_answer.question, question)
        self.assertEqual(second_saved_answer.text, 'The Answer B')
        self.assertEqual(second_saved_answer.question, question)
        self.assertEqual(third_saved_answer.text, 'The Answer C')
        self.assertEqual(third_saved_answer.question, question)
        self.assertEqual(fourth_saved_answer.text, 'The Answer D')
        self.assertEqual(fourth_saved_answer.question, question)
