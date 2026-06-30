from datetime import datetime, timedelta
from habits.models import Habit
from django.db.models import Count

class HabitTrackerService:
    def get_user_habits(self, user_id):
        return Habit.objects.filter(user_id=user_id)

    def create_habit(self, user_id, name, category, frequency):
        habit = Habit(user_id=user_id, name=name, category=category, frequency=frequency)
        habit.save()
        return habit

    def update_habit(self, habit_id, name, category, frequency):
        habit = Habit.objects.get(id=habit_id)
        habit.name = name
        habit.category = category
        habit.frequency = frequency
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
                'category': habit.category,
                'frequency': habit.frequency,
                'streak': self.get_habit_streak(habit)
            }
            stats.append(habit_stats)
        return stats

    def get_habit_streak(self, habit):
        today = datetime.today()
        streak = 0
        for i in range(30):
            date = today - timedelta(days=i)
            if habit.checkins.filter(date=date).exists():
                streak += 1
            else:
                break
        return streak