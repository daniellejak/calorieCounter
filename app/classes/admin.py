from django.contrib import admin

# Register your models here.
from .models import dailyLog
admin.site.register(dailyLog)
from .models import exercises
admin.site.register(exercises)
from .models import food
admin.site.register(food)
from .models import logHasExercise
admin.site.register(logHasExercise)
from .models import logHasFood
admin.site.register(logHasFood)
from .models import user
admin.site.register(user)

