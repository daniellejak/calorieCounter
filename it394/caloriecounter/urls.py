from django.urls import path

from . import views

app_name='calorieCounter'
urlpatterns = [
    path('',views.index,name='index'),
    path('exercises/',views.exercises, name='exercises'),
]
