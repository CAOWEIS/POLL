from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Question(BaseModel):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    question_text = models.CharField(max_length=200)
    is_draft = models.BooleanField(default=True)
    end_date = models.DateTimeField(null=True, blank=True, verbose_name='结束日期')
    objects = None

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
