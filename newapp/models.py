from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=200)
    age = models.IntegerField(
        validators=[MinValueValidator(18),MaxValueValidator(30)]
    )
    hobby = models.CharField(max_length=500)
    image=models.CharField(max_length=1000,default='https://atlas-content-cdn.pixelsquid.com/stock-images/cartoon-boy-8JY1YDF-600.jpg')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('newapp:detail',kwargs={'pk':self.pk})