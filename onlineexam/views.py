from django.shortcuts import render
from .models import Question

def home_page(request):
    first_question = Question.objects.first()

    return render(request, 'onlineexam/home.html', {'question': first_question})
