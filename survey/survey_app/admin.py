from django.contrib import admin

# Register your models here.
from .models import Question, Survey, Choice, SurveyAnswer, QuestionAnswer

admin.site.register(Question)
admin.site.register(Survey)
admin.site.register(Choice)
admin.site.register(SurveyAnswer)
admin.site.register(QuestionAnswer)