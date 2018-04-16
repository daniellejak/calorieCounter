from django.db import models

# Create your models here.
class exercises(models.Model):
    exerciseName = models.CharField(max_length=75)
    caloriesPerMin = models.IntegerField()

class food(models.Model):
    foodName = models.CharField(max_length=75)
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    protein = models.IntegerField()

class logHasFood(models.Model):
    foodName = models.CharField(max_length=75)
    user = models.IntegerField()

class dailyLog(models.Model):
    user = models.CharField(max_length=75)
    date = models.DateField()
    
class user(models.Model):
    user = models.CharField(max_length=75)
    firstName = models.CharField(max_length=75)
    lastName = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    
class logHasExercise(models.Model):
    exerciseName = models.CharField(max_length=75)
    user = models.ForeignKey(user, on_delete=models.CASCADE,default=1)
    minsExercised = models.IntegerField()





