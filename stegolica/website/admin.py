from django.contrib import admin

# Register your models here.
from .models import Question,Ranking,Answers

mymodels=[Question,Ranking,Answers]
admin.site.register(mymodels)
