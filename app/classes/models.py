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


class user(models.Model):
    firstName = models.CharField(max_length=75)
    lastName = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    
    
class logHasFood(models.Model):
    foodName = models.CharField(max_length=75)
    user = models.ForeignKey(user, on_delete=models.CASCADE,default=1)

class dailyLog(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE,default=1)
    date = models.DateField()
    
    
class logHasExercise(models.Model):
    exerciseName = models.CharField(max_length=75)
    user = models.ForeignKey(user, on_delete=models.CASCADE,default=1)
    minsExercised = models.IntegerField()





