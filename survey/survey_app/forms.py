from django import forms
from .models import Survey, Question, Choice



class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = "__all__" 

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = "__all__"