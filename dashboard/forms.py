from django import forms
from django.contrib.auth.models import User ,  UserCreationForm
from .models import Question , Answers , quiztaker
from django.db import transaction
from django.forms.utils import ValidationError

class QuestionCreateForm(forms.ModelForm):
    question = forms.CharField()
    class Meta :
        model = Question
        fields = ['question'] 

class AnswerCreateForm(forms.ModelForm):
    option_1 = forms.CharField()
    option_2 = forms.CharField()
    option_3 = forms.CharField()
    option_4 = forms.CharField()
    option1_is_correct = forms.BooleanField(required=False)
    option2_is_correct = forms.BooleanField(required=False)
    option3_is_correct = forms.BooleanField(required=False)
    option4_is_correct = forms.BooleanField(required=False)

    class Meta : 
        model = Answers
        fields = ['option_1','option1_is_correct','option_2','option2_is_correct','option_3','option3_is_correct','option_4','option4_is_correct']

class QTSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_quiztaker = True
        user.save()
        return user

class QMSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_quizmaster = True
        if commit:
            user.save()
        return user