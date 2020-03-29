from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=130, blank=False)
    mobile_number = models.IntegerField(max_length=10, blank=False)
    email = models.EmailField(blank=False)
    address = models.TextField(blank=True)
