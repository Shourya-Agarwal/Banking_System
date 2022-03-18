from django.db import models

class Customers(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField(unique=True)
    credits=models.FloatField()
    def __str__(self):
        return self.name

class transactions(models.Model):
    from1=models.CharField(max_length=50)
    to1=models.CharField(max_length=50)
    amount=models.FloatField()
    