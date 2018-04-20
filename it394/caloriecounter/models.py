from django.db import models


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


class User(models.Model):
    firstName = models.CharField(max_length=75)
    lastName = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    
    
class LogHasFood(models.Model):
    foodName = models.CharField(max_length=75)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date = models.DateField()
    
    
class LogHasExercise(models.Model):
    exerciseName = models.CharField(max_length=75)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    minsExercised = models.IntegerField()





