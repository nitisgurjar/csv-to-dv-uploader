from django.db import models

# Create your models here
class Csvv(models.Model):
    Name=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=50)
    Email=models.EmailField(max_length=254)
    Address=models.CharField(max_length=50)

    def __str__(self)->str:
        return self.name
    