from django.db import models
from django.contrib.auth import get_user_model
from habits.models import Habit

class UserHabit(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s {self.habit.name} habit"

    class Meta:
        unique_together = ('user', 'habit')
        ordering = ['created_at']