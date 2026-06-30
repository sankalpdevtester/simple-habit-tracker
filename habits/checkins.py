from django.db import models
from habits.models import Habit

class Checkin(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='checkins')
    date = models.DateField()

    def __str__(self):
        return f'{self.habit.name} - {self.date}'

class CheckinService:
    def create_checkin(self, habit_id, date):
        checkin = Checkin(habit_id=habit_id, date=date)
        checkin.save()
        return checkin

    def get_checkins(self, habit_id):
        return Checkin.objects.filter(habit_id=habit_id)

    def delete_checkin(self, checkin_id):
        checkin = Checkin.objects.get(id=checkin_id)
        checkin.delete()