from django import forms

from .models import Question,Answers

class QuestionForm(forms.ModelForm):
    class Meta:
		model=Answers
		fields=[
		"answer"
        ]
