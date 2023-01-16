from django.shortcuts import render , redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from .forms import QTSignUpForm , QMSignUpForm

# Create your views here.

def home(request):
    return render(request , 'dashboard/home.html' )
    
# class QuizListView(ListView):
#     model = Quiz
#     template_name = 'Quiz/quiz_home.html'
#     context_object_name = 'quiz'

# class QuizDetailView(DetailView):
#     model = Quiz
#     template_name = 'Quiz/quiz_information.html'
    
# def QuestionView(request , id ):
#     ques = Question.objects.all()
#     ans = Answer.objects.all()
#     quiz = Quiz.objects.all()
#     id_no = Quiz.objects.get(id = id)
#     content = { 'id' : id_no ,'quiz' : quiz , 'question' : ques , 'answer' : ans}
#     return render(request , 'Quiz/question.html' , content)

