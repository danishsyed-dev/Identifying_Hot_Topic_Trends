from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=128)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class predict_hot_topic(models.Model):

    Sno= models.CharField(max_length=300)
    PDate= models.CharField(max_length=300)
    Headline= models.CharField(max_length=3000)
    Description= models.CharField(max_length=3000)
    Source= models.CharField(max_length=3000)
    Prediction= models.CharField(max_length=300)

    def __str__(self):
        return f"{self.Headline} - {self.Prediction}"

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.names}: {self.ratio}"

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.names}: {self.ratio}"
