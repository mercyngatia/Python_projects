from django.db import models

# Create your models here.

class Course(models.Model):
    Title = models.CharField(max_length = 30)
    Location = models.CharField(max_length = 30)
    Trainer = models.CharField(max_length = 30)
    
    def __str__ (self):
        return self.Title

class Teacher(models.Model):
    Name=models.CharField(max_length= 30)
    Course=models.CharField(max_length= 30)
    Description = models.CharField(max_length= 100)
    Availability = models.CharField(max_length=30)

def __str__(self):
    return self.names
    
    
class Food(models.Model):
    Cuisine =models.CharField(max_length=20)
    Ingredients =models.CharField(max_length= 50)
    Methods =models.TextField(max_length=100)
    Pub_date =models.DateTimeField('date published')
    
    