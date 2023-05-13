from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.survey_home, name='survey_home'),
    path('postsurvey/', views.postsurvey, name='postsurvey/'),
]