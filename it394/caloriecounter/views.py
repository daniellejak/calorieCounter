from django.shortcuts import render
from django.template import loader
from .models import Exercises
from .models import DailyLog
from .models import LogHasFood
from .models import LogHasExercise
from .models import Food
from django.http import HttpResponse
from django.http import HttpResponseRedirect

#from .forms import CadetForm

# Create your views here.
def exercises(request):
    exercises = Exercises.objects.all() #Grab all cadets from database
    context = {'exercises': exercises} #fill a context with the cadet list
    template = loader.get_template('caloriecounter/exercises.html') #Get the template we created
    return HttpResponse(template.render(context, request)) #Render the template with the context
    
def index(request):
    dailylog = DailyLog.objects.get(pk=1)
    foodlog = LogHasFood.objects.filter(dailyLog = dailylog.id)
    exerciselog = LogHasExercise.objects.filter(dailyLog = dailylog.id)
    totalcalories = 0
    totalcarbs = 0
    totalfat = 0
    totalprotein = 0
    for food in foodlog:
        totalcalories = food.foodName.calories + totalcalories
    for carbs in foodlog:
        totalcarbs = food.foodName.carbs + totalcarbs
    for fat in foodlog:
        totalfat = food.foodName.fat + totalfat 
    for protein in foodlog:
        totalprotein = food.foodName.protein + totalprotein
        
    context = {'dailylog': dailylog, 'foodlog' : foodlog, 'exerciselog' : exerciselog, 'totalcalories' : totalcalories, 'totalcarbs' : totalcarbs, 'totalfat' : totalfat, 'totalprotein' : totalprotein} #fill a context with the cadet list
    template = loader.get_template('caloriecounter/index.html') #Get the template we created
    return HttpResponse(template.render(context, request)) #Render the template with the context

def detail(request, exercise_id):
    try:
        exercise = Exercises.objects.get(pk=exercise_id)
        context = {'exercise':exercise}
    except Exercises.DoesNotExist:
        raise Http404("Exercises does not exist")
    return render(request, 'caloriecounter/detail.html', context)
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

