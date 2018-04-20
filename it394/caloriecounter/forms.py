from .models import Exercise, User, LogHasFood, DailyLog, LogHasExercise

from django import forms



class ExerciseForm(forms.ModelForm):

    class Meta:

        model = Exercise

        fields = '__all__'

class UserForm(forms.ModelForm):

    class Meta:

        model = User

        fields = '__all__'

class LogHasFood(forms.ModelForm):

    class Meta:

        model = LogHasFood

        fields = '__all__'

class DailyLog(forms.ModelForm):

    class Meta:

        model = DailyLog

        fields = '__all__'



