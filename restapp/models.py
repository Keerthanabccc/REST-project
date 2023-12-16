from django.db import models

# Create your models here.



class todos(models.Model):
    taskname=models.CharField(max_length=50)
    user=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    date=models.DateField(auto_now=True)


# class movies(models.Model):
#     name=models.CharField(max_length=50)
#     reldate=models.DateField()
#     char=models.CharField(max_length=50)
#     thenme=models.CharField(max_length=50)
#     dirnme=models.CharField(max_length=50)
#     rating=models.BooleanField()
    # is_active=models.BooleanField(default=True)
    # date=models.DateField()