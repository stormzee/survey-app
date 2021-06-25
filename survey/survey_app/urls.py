from django.urls import path
from .views import index, survey, create_survey,Add_question, question_success, survey_success,Add_choice,choice_success

urlpatterns = [
    path('', index, name='index'),
    path('survey/<int:id>/', survey, name='survey'),
    path('createsurvey/', create_survey, name='createsurvey'),
    path('survey_success/', survey_success, name='survey_success'),
    path('add_question/', Add_question, name='add_questions'),
    path('question_success/', question_success, name='question_success'),
    path('add_choice/', Add_choice, name='add_choices'),
    path('choice_success/', choice_success, name='choice_success'),
]
