from .models import Exercises, LogHasFood, DailyLog, LogHasExercise, Food

from django import forms



class ExerciseForm(forms.ModelForm):

    class Meta:

        model = LogHasExercise

        fields = ('exerciseName'),('minsExercised'),
        labels = {
            'exercise': ('Enter exercise'),
            'duration': ('time exercised'),
                }
        
        
class FoodForm(forms.ModelForm):

    class Meta:
        model = LogHasFood
        fields = ('foodName'),
        labels = {
            'name': ('Enter food'),
            }

class DailyLog(forms.ModelForm):

    class Meta:

        model = DailyLog

        fields = '__all__'
        
class Food(forms.ModelForm):

    class Meta:

        model = Food

        fields = '__all__'



