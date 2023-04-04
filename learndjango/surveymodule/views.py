from django.shortcuts import render
from .models import *
# Create your views here.

def survey_home(request):
    surveys = Survey.objects.all()

    return render(request, 'surveymodule/survey_home.html', {'surveys': surveys})