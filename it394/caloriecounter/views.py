from django.shortcuts import render, redirect
from django.template import loader
from .models import Exercises
from .models import DailyLog
from .models import LogHasFood
from .models import LogHasExercise
from .models import Food
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

from .forms import FoodForm
from .forms import ExerciseForm

# Create your views here.
def exercises(request):
    exercises = Exercises.objects.all() #Grab all cadets from database
    context = {'exercises': exercises} #fill a context with the cadet list
    template = loader.get_template('caloriecounter/exercises.html') #Get the template we created
    return HttpResponse(template.render(context, request)) #Render the template with the context
    
def index(request):
    currentDate = datetime.now().date() 
    try:
        dailylog = DailyLog.objects.get(date=currentDate)

    except:
        dailylog = DailyLog(date = currentDate)
        if request.user.is_authenticated:
            dailylog.user=request.user
            dailylog.save()
        else:
            return HttpResponseRedirect('/accounts/login')
    #    LogHasFood.objects.all().delete()
    #    LogHasExercise.objects.all().delete()  
    full_log = DailyLog.objects.all()
    foodlog = LogHasFood.objects.filter(dailyLog = dailylog.id)
    logexercises = LogHasExercise.objects.filter(dailyLog = dailylog.id)
    #exercises = Exercises.objects.filter(dailyLog = dailylog.id)
    foodcalories = 0
    exercisecalories = 0
    totalcarbs = 0
    totalfat = 0
    totalprotein = 0
    for food in foodlog:
        foodcalories = food.foodName.calories + foodcalories #- exercise.exerciseName.caloriesPerMin
    for el in logexercises:
        exercisecalories = exercisecalories + el.minsExercised * el.exerciseName.caloriesPerMin
        #exercise = Exercises.objects.filter(exerciseName = exercise.exerciseName)
        #for calPerMin in calsPerMin:
        #    exercisecalories = exercise.minsExercised*calsPerMin +exercisecalories
    for carbs in foodlog:
        totalcarbs = food.foodName.carbs + totalcarbs
    for fat in foodlog:
        totalfat = food.foodName.fat + totalfat 
    for protein in foodlog:
        totalprotein = food.foodName.protein + totalprotein
    totalcalories = foodcalories - exercisecalories
        
    context = {'dailylog': dailylog, 'foodlog' : foodlog, 'logexercises' : logexercises, 'totalcalories' : totalcalories, 'totalcarbs' : totalcarbs, 'totalfat' : totalfat, 'totalprotein' : totalprotein, 'full_log' : full_log} #fill a context with the cadet list
    template = loader.get_template('caloriecounter/index.html') #Get the template we created
    return HttpResponse(template.render(context, request)) #Render the template with the context

def detail(request, exercise_id):
    try:
        exercise = Exercises.objects.get(pk=exercise_id)
        context = {'exercise':exercise}
    except Exercises.DoesNotExist:
        raise Http404("Exercises does not exist")
    return render(request, 'caloriecounter/detail.html', context)
    
def addfood(request, dailylog_id):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            dailyLog = DailyLog.objects.get(pk=dailylog_id)
            #Add the cadet to the database
            newfood = form.save()
            #newfood = LogHasFood.objects.get(pk=newfood.id)
            newfood.dailyLog = dailyLog
            newfood.save()
            #Go back to cadet list
            return HttpResponseRedirect('/caloriecounter')
    else:
        form = FoodForm()
    return render(request, 'caloriecounter/food/add.html', {'form': form})
    
def addexercise(request, dailylog_id):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            dailyLog = DailyLog.objects.get(pk=dailylog_id)
            #Add the cadet to the database
            newexercise = form.save()
            newexercise.dailyLog = dailyLog
            newexercise.save()
            #Go back to cadet list
            return HttpResponseRedirect('/caloriecounter')
    else:
        form = ExerciseForm()
    return render(request, 'caloriecounter/loghasexercise/add.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/caloriecounter')
    else:
        form = UserCreationForm()
    return render(request, 'caloriecounter/signup.html', {'form': form})

'''
def update(request, cadet_id):
    new_xnumber = request.POST['xnumber']
    new_company_id = request.POST['company_id']
    cadet = Cadet.objects.get(pk=cadet_id)
    cadet.xnumber = new_xnumber
    cadet.company_id = new_company_id
    cadet.save()
    companies = Company.objects.all()
    context = {'cadet':cadet, 'companies': companies}
    return render(request, 'users/detail.html', context)

def addcadet(request):
    if request.method == 'POST':
        form = CadetForm(request.POST)
        if form.is_valid():
            #Add the cadet to the database
            newcadet = form.save()
            #Go back to cadet list
            return HttpResponseRedirect('/users')
    else:
        form = CadetForm()
return render(request, 'users/add.html', {'form': form})'''

