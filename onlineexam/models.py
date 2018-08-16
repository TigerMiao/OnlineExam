from django.db import models

class Question(models.Model):
    text = models.TextField(default='')

class Answer(models.Model):
    text = models.TextField(default='')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
