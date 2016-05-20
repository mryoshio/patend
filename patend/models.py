from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)
    pricing = models.BooleanField(default=False)

class Office(models.Model):
    name = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=30)
    token = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Record(models.Model):
    office = models.ForeignKey(Office)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
