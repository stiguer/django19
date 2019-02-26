from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Envelope(models.Model):
    amount = models.IntegerField()
    motivation = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.company.name+" "+self.motivation
