from rest_framework import serializers
from .models import Habit, HabitLog, HabitCategory

class HabitCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitCategory
        fields = ['id', 'name']

class HabitSerializer(serializers.ModelSerializer):
    category = HabitCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source='category', queryset=HabitCategory.objects.all(), write_only=True
    )

    class Meta:
        model = Habit
        fields = ['id', 'user', 'category', 'category_id', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

class HabitLogSerializer(serializers.ModelSerializer):
    habit = HabitSerializer(read_only=True)
    habit_id = serializers.PrimaryKeyRelatedField(
        source='habit', queryset=Habit.objects.all(), write_only=True
    )

    class Meta:
        model = HabitLog
        fields = ['id', 'habit', 'habit_id', 'log_date', 'completed']
        read_only_fields = ['id']

    def validate_habit_id(self, habit):
        request = self.context.get('request')
        if request and habit.user_id != request.user.id:
            raise serializers.ValidationError('You can only log your own habits.')
        return habit
