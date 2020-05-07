from django.db import models

# Create your models here.
class Sentence(models.Model):
  value = models.TextField(blank=False)