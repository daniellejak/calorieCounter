from django.contrib import admin

# Register your models here.

from .models import Food
from .models import Exercises
from .models import LogHasFood
from .models import DailyLog
from .models import LogHasExercise


admin.site.register(Food)
admin.site.register(Exercises)
admin.site.register(LogHasFood)
admin.site.register(DailyLog)
admin.site.register(LogHasExercise)
