from django.shortcuts import render
from .models import *
from .businesslogic.connect_to_kardionet import *

# Create your views here.

def survey_home(request):
    surveys = Survey.objects.filter(
        title='Первая стадия'
    )
    print(surveys[0])
    return render(request, 'surveymodule/survey_home.html', {'survey': surveys[0]})

def postsurvey(request):

    questions = [""] * 30
    date = request.POST.get("q1")
    questions[0] = request.POST.get("q2")#возраст
    questions[28] = request.POST.get("q4")#рост
    questions[29] = request.POST.get("q5")#вес
    print(questions)
    for item in request.POST:
        values = request.POST.get(item).split(';')
        print(values)
        if len(values) > 1:
            questions[int(values[1])] = values[0]

    print(questions)
    print(UseProgramNew(CreateDiag(1, date, questions)))


    surveys = Survey.objects.filter(
        title='Первая стадия'
    )
    return render(request, 'surveymodule/survey_home.html', {'survey': surveys[0]})