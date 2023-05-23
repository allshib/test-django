from django.shortcuts import render
from .models import *
from .businesslogic.connect_to_kardionet import *
from .businesslogic.surveylogic import *
import django

# Create your views here.

def survey_home(request):
    surveys = Survey.objects.filter(
        title='Первая стадия'
    )
    print(surveys[0])
    return render(request, 'surveymodule/survey_home.html', {'survey': surveys[0]})

def postsurvey(request, params):

    if params == 'SERVER' and not request.POST:
        return render(request, 'surveymodule/empty_result.html')
    user_notiffication = None
    result = None
    changes = None
    if params == 'SERVER':
        questions = ["0"] * 31
        date = request.POST.get("q1").split('-')
        date = date[2] + "." + date[1] + "." + date[0]
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

        for i in range(0, len(questions)):
            questions[i] = GetStringNumber(questions[i])

        print(django.get_version())

        result = GetResultArr(1, date, questions)
        print(result)
    else:
        result = ParseURLParams(params)
        user_notiffication = AnalyzeResultsAndGetNotificationForUser(result)
        changes = SearchChanges([90.28, 90.02, 20.32, 92.32, 10.2, 3.33, 50.14, 6.45], result)
    # result = [90.28, 6.02, 92.32, 92.32, 10.2, 3.33, 2.14, 6.45]
    if result == None:
        return render(request, 'surveymodule/empty_result.html')

    return render(request, 'surveymodule/survey_result.html', {'result': result, 'notification': user_notiffication})


def test_result(request):
    return render(request, 'surveymodule/survey_result.html')