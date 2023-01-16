from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    is_quiztaker = models.BooleanField(default=False)
    is_quizmaster = models.BooleanField(default=False)

class Quizzes(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)    
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="Set time for the test in seconds")
    
    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()
    
    def get_absolute_url(self):    
        return reverse('new-ques' , kwargs={'id' : self.pk})


class Question(models.Model):
    content = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    
    def get_answers(self):
        return self.answer_set.all()

class Answers(models.Model):
    content = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"question: {self.question.content}, answer: {self.content}, correct: {self.correct}"


class quiztaker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quizzes, through='TakenQuiz') #through is to manually specify intermediatry table

    def __str__(self):
        return self.user.username


class TakenQuiz(models.Model):
    student = models.ForeignKey(quiztaker , on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)


class QTAnswer(models.Model):
    student = models.ForeignKey(quiztaker , on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='+')