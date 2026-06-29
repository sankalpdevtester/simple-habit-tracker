from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class HabitCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(HabitCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    log_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.habit.name} - {self.log_date}'