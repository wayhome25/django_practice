# polls_cbv.models
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('작성일시')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question) # Question : Choice = 1 : N 관계
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
