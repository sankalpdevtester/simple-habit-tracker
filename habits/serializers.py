from rest_framework import serializers
from .models import Habit, HabitLog, HabitCategory

class HabitCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitCategory
        fields = ['id', 'name']

class HabitSerializer(serializers.ModelSerializer):
    category = HabitCategorySerializer(read_only=True)

    class Meta:
        model = Habit
        fields = ['id', 'user', 'category', 'name', 'description', 'created_at']

class HabitLogSerializer(serializers.ModelSerializer):
    habit = HabitSerializer(read_only=True)

    class Meta:
        model = HabitLog
        fields = ['id', 'habit', 'log_date', 'completed']