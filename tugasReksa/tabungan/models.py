from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(primary_key=True, max_length=100)
    fullName = models.CharField(max_length=100)
    address  = models.TextField()
    dateReg = models.DateField()
    exp = models.FloatField()
    level = models.FloatField()    

    def __str__(self):
        return self.userName

class ReksaDana(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    unitNumber = models.FloatField()
    userName = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name