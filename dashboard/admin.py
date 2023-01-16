from django.contrib import admin
from .models import User , Quizzes , Question , Answers , quiztaker , TakenQuiz , QTAnswer
# Register your models here.

mymodel = [User , Quizzes , Question , Answers  , quiztaker , TakenQuiz , QTAnswer ]
admin.site.register(mymodel)
