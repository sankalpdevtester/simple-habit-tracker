from django.contrib import admin
from .models import Habit, HabitLog, HabitCategory

admin.site.register(Habit)
admin.site.register(HabitLog)
admin.site.register(HabitCategory)