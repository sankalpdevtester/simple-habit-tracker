from datetime import timedelta

from django.utils import timezone
from habits.models import Habit, HabitCategory, HabitLog

class HabitTrackerService:
    def get_user_habits(self, user_id):
        return Habit.objects.filter(user_id=user_id)

    def create_habit(self, user_id, name, category, description=""):
        category_id = category.pk if isinstance(category, HabitCategory) else category
        return Habit.objects.create(
            user_id=user_id,
            name=name,
            category_id=category_id,
            description=description,
        )

    def update_habit(self, habit_id, name, category, description=None):
        habit = Habit.objects.get(id=habit_id)
        habit.name = name
        habit.category_id = category.pk if isinstance(category, HabitCategory) else category
        if description is not None:
            habit.description = description
        habit.save()
        return habit

    def delete_habit(self, habit_id):
        habit = Habit.objects.get(id=habit_id)
        habit.delete()

    def get_habit_stats(self, user_id):
        habits = Habit.objects.filter(user_id=user_id)
        stats = []
        for habit in habits:
            habit_stats = {
                'name': habit.name,
                'category': habit.category.name,
                'streak': self.get_habit_streak(habit)
            }
            stats.append(habit_stats)
        return stats

    def get_habit_streak(self, habit):
        today = timezone.localdate()
        if not HabitLog.objects.filter(habit=habit, log_date=today, completed=True).exists():
            today -= timedelta(days=1)
        streak = 0
        for i in range(30):
            date = today - timedelta(days=i)
            if HabitLog.objects.filter(habit=habit, log_date=date, completed=True).exists():
                streak += 1
            else:
                break
        return streak
