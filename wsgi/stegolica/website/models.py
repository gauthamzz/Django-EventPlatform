from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class Question(models.Model):
    questionid = models.AutoField(primary_key=True)
    questiontext = models.CharField(max_length=100)
    answertext = models.CharField(max_length=100)
    hint1 = models.CharField(max_length=300, default="No Hints")
    imagelink = models.CharField(max_length=300, default="No Image/Video")

    def __unicode__(self):
        return unicode(self.questionid)

    def __str__(self):
        return self.questionid

    def get_absolute_url(self):
        return reverse("website:questions", kwargs={"id": self.questionid})


class Ranking(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    currentquestion = models.CharField(max_length=100)
    timestarted = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return unicode(self.username)

    def __str__(self):
        return self.username


class Answers(models.Model):
    answerid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.username)

    def __str__(self):
        return self.username
