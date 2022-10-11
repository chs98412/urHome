from django.db import models

# Create your models here.
class bad(models.Model):
    who = models.TextField()
    when = models.TextField()
    what = models.TextField()
    why = models.TextField()

class money(models.Model):
    name= models.TextField(null=True)
    total=models.IntegerField()