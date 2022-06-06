from django.db import models


class CitizenInfo(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    landline = models.CharField(max_length=100)
    cell_phone = models.CharField(max_length=100)
    been_infected = models.BooleanField(default=False)
    conditions = models.CharField(max_length=100,blank=True)
