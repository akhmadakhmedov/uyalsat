from django.db import models

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

