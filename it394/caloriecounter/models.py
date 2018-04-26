from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exercises(models.Model):
    exerciseName = models.CharField(max_length=75)
    caloriesPerMin = models.IntegerField()

class Food(models.Model):
    foodName = models.CharField(max_length=75)
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    protein = models.IntegerField()

class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date = models.DateField()
    
    def __str__(self):
        return (self.user.username + ": " + str(self.date)) 
         
           
class LogHasFood(models.Model):
    foodName = models.ForeignKey(Food, on_delete=models.CASCADE,default=1)
    dailyLog = models.ForeignKey(DailyLog, on_delete=models.CASCADE,default=1)
    

class LogHasExercise(models.Model):
    exerciseName = models.ForeignKey(Exercises, on_delete=models.CASCADE,default=1)
    minsExercised = models.IntegerField()
    dailyLog = models.ForeignKey(DailyLog, on_delete=models.CASCADE,default=1)





