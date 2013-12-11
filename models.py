from django.db import models

class Session(models.Model):
    questions = models.CharField(max_length=200, default = '', blank=True)

class Question(models.Model):
    photo_id = models.IntegerField()
    gif = models.BooleanField(default=False)
    correct = models.BooleanField(default=False)
