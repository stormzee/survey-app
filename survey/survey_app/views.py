from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Question, Choice, Survey, QuestionAnswer, SurveyAnswer, user

# from django.contrib.sessions import session
# Create your views here.

def index(request):
    surveys = Survey.objects.all()
    ctx = {'surveys':surveys}
    return render(request, 'index.html', ctx)


# filling the survey.... let's grab the id(by passsing the id argument to the survey view) 
# of the survey which the user clicked

def survey(request, id):
    survey = get_object_or_404(Survey, pk=id)
    # filter and display all questions based on the survey we are currently viewing
    # For example, we can get all questions in a survey by using .... Survey.question_set.all 
    # if only they are related by a ForeignKey relationship 
    questions = Question.objects.filter(survey=survey)
    if request.method == 'POST':
        # if there is a post request, let's create a SurveyAnswer object (bcus we are filling a survey
        # which will be saved in the surveyAnswer model)
        answer = SurveyAnswer()
        # let's set the attributess of a surveyAnswer object..
        # using the dot notation, the name of the object.attribute
        # set the survey attribute of the SurveyAnswer object to the survey we are currently viewing
        answer.survey = survey
        # save the SurveyAnswer object
        answer.save()
        # get all the answers chosen by a user for each question
        # for every question in the survey, Grab the question
        for question in questions:
            #  get the choice chosen by user
            qc = request.POST[str(question.id)]
            # print(qc)
            # Create a QuestionAnswer object for each answer to a question
            QA = QuestionAnswer()
            # set the answer of a question by getting the choice chosen by the user
            QA.answer = Choice.objects.get(id = qc)
            # print(QA.answer)

            # set the survey_answer attribute to the SurveyAnswer object and
            #  save the question answer.
            QA.survey_answer = answer
            QA.save()

            # save all answers to the surveyanswer object (bcuz a user has 
            # provided answers for that 
            # particular survey) after making changes to the SurveyAnswer model
        answer.save()
    ctx = {'questions':questions}
    return render(request, 'survey.htm', ctx)

# create a survey
# we'll this with html form
# we'll create a Survey object
# get the title of the survey by using html user input
# set the creator to the logged in user
# save the Survey instance to the database
# Grab the current survey using 'session' 
# with sessions, data is lost when browser is closed
# 

def create_survey(request):
    if request.method == 'POST':
        new_survey = Survey()
        new_survey.title = request.POST['survey_title']
        new_survey.creator = request.user
        new_survey.save()
        request.session['current_survey'] = new_survey.id
        # print(request.session['current_survey'])
        return redirect('survey_success')
    return render(request, 'create_survey.htm')

def survey_success(request):
    return render(request, 'survey_create_success.htm')
# Adding questions to a Survey

# Note :

def Add_question(request):
    if request.method == 'POST':
        # Get the current survey from the session data by using the 'objects.get' method
        question_survey = Survey.objects.get(id= int(request.session['current_survey']))
        # after getting the current survey, create a question 
        # by creating a Question instance new_question
        new_question = Question()
        # Set the attributes of the new_question (Question instance) using the html user input
        new_question.question_text = request.POST['question']
        # Database methods can be executed from the django app..
        # methods such as add, exists, delete, get are used to perform actions on a db model.
        question_survey.question_set.add(new_question, bulk=False)
        new_question.save()
        question_survey.save()
        request.session['current_question'] = new_question.id
        return redirect('question_success')
    return render(request, 'add_question.htm')


def question_success(request):
    return render(request, 'question_success.htm')


def Add_choice(request):

    if request.method == 'POST':
        # grab the question
        question = Question.objects.get(id = int(request.session['current_question']))
        # create a new choice object
        new_choice = Choice()
        # set attributes of the new choice object(choice_text, question)
        new_choice.choice_text = request.POST['choice']
        # add the new choice to the choices of the selected question
        question.choice_set.add(new_choice, bulk=False)
        # save the new choice object created
        new_choice.save()
        # save the question object after adding choice to the choice_set of the question
        question.save()
        return redirect('choice_success')
    return render(request, 'choices.htm')

def choice_success(request):
    return render(request, 'choice_success.htm')

#  view to handle the user profile
# thus, survey answers conresponding to each
# try to distinguish surveys by associating each surveyanswer object with a particular user
# 
