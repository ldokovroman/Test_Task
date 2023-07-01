from django.db import models

class Request(models.Model):
    text = models.TextField()
