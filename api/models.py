from django.db import models

class Submission(models.Model):
    character = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
