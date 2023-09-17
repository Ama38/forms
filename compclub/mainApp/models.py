from django.db import models
from mainApp.validators import capitalLetterValidator
# Create your models here.


class CompClub(models.Model):
    name = models.CharField(max_length=50, validators=[capitalLetterValidator])
    surname = models.CharField(max_length=50, validators=[capitalLetterValidator])
    middlename = models.CharField(max_length=50, validators=[capitalLetterValidator])
    email = models.EmailField()
    desired_place = models.CharField(max_length=50)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField()
    vip = models.BooleanField()
    promo_code = models.CharField(default='', max_length=50)
    commentaries = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.surname}"
    

