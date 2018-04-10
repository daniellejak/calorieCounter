from django.db import models

# Create your models here.
class exercises(models.Model):
    exerciseName = models.CharField(max_length=75, primary_key = True)
    caloriesPerMin = models.IntegerField()

class food(models.Model):
    foodName = models.CharField(max_length=75, primary_key = True)
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    protein = models.IntegerField()

class logHasFood(models.Model):
    foodName = models.CharField(max_length=75, primary_key = True)
    userID = models.IntegerField(primary_key = True)

class dailyLog(models.Model):
    userID = models.CharField(max_length=75, primary_key = True)
    date = models.DateField()

class logHasExercise(models.Model):
    exerciseName = models.CharField(max_length=75, primary_key = True)
    userID = models.IntegerField(primary_key = True)
    minsExercised = models.IntegerField()

class user(models.Model):
    userID = models.CharField(max_length=75, primary_key = True)
    firstName = models.CharField(max_length=75)
    lastName = models.CharField(max_length=75)
    password = models.CharField(max_length=75)



