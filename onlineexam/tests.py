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

class QuestionViewTest(TestCase):
    def test_display_first_question(self):
        Question.objects.create(text='The first question')
        Question.objects.create(text='The second question')

        response = self.client.get('/')

        self.assertContains(response, '1. The first question')
        self.assertNotContains(response, '2. The second question')

class AnswerModelTest(TestCase):

    def test_save_and_retrieving_answer(self):
        question = Question()
        question.text = "The first question"
        question.save()

        answerA = Answer()
        answerA.text = "The Answer A"
        answerA.question = question
        answerA.save()

        answerB = Answer()
        answerB.text = "The Answer B"
        answerB.question = question
        answerB.save()

        answerC = Answer()
        answerC.text = "The Answer C"
        answerC.question = question
        answerC.save()

        answerD = Answer()
        answerD.text = "The Answer D"
        answerD.question = question
        answerD.save()

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
