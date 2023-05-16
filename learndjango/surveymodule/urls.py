from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.survey_home, name='survey_home'),
    path('postsurvey/<params>', views.postsurvey, name='postsurvey/'),
    path('test_result/', views.test_result, name='testresult/'),

]