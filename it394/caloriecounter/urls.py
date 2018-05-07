from django.urls import path
from django.conf.urls import url
#from caloriecounter.core import views as core_views

from . import views

app_name='caloriecounter'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:exercise_id>/',views.detail,name='detail'),
    path('exercises',views.exercises, name='exercises'),
    path('food/add/<int:dailylog_id>',views.addfood,name='addfood'),
    path('loghasexercise/add/<int:dailylog_id>',views.addexercise,name='addexercise'),
    path('signup', views.signup, name='signup'),
]
