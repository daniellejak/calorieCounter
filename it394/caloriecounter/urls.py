from django.urls import path

from . import views

app_name='caloriecounter'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:exercise_id>/',views.detail,name='detail'),
    path('exercises',views.exercises, name='exercises'),
    path('food/add/<int:dailylog_id>',views.addfood,name='addfood'),
    path('exercise/add/<int:dailylog_id>',views.addexercise,name='addexercise'),
]
