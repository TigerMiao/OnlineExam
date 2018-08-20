from django.shortcuts import render
from .models import Question

def home_page(request):
    if request.method == 'POST':
        question_id = request.POST['question_id']
        next_or_last = request.POST['next_or_last']

        if next_or_last == 'next':
            if int(question_id) < Question.objects.count():
                question_id = str(int(question_id) + 1)
        else:
            if int(question_id) > 1:
                question_id = str(int(question_id) - 1)

        question = Question.objects.get(id=question_id)
        return render(request, 'onlineexam/home.html', {'question': question})

    first_question = Question.objects.first()

    return render(request, 'onlineexam/home.html', {'question': first_question})
