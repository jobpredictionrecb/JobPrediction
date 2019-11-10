from django.db import models

class FeedbackModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    feedback = models.CharField(max_length=500)
