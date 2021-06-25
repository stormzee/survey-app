from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model

# Create your models here.
user = get_user_model()


class Survey(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(user, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

# _set.all can be used to get data from a Foreignkey related model
#E.g. we can retrieve all questions of a particular survey by using survey.question_set.all
# Also, we can get all choices in a question by question.choice_set.all
# get all surveyAnswers of a particular survey by survey.SurveyAnswer_set.all
# get all questionAnswers of a particular survey by survey_answer.QuestionAnswer_set.all

class  Question(models.Model):
    question_text = models.CharField(max_length=500)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=225)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self): 
        return self.choice_text
    

# this model saves the survey
class SurveyAnswer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.survey.title
    

# this model saves the answers to a particular question which is also related to a specific survey
class QuestionAnswer(models.Model):
    answer = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    survey_answer = models.ForeignKey(SurveyAnswer, on_delete=models.CASCADE)

    def __str__(self):
        return self.survey_answer.survey.title
    


    

    