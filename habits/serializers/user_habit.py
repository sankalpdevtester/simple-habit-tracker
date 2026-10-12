from rest_framework import serializers
from habits.models import Habit, UserHabit
from habits.serializers import HabitSerializer

class UserHabitSerializer(serializers.ModelSerializer):
    habit = HabitSerializer(read_only=True)
    habit_id = serializers.PrimaryKeyRelatedField(
        source='habit', queryset=Habit.objects.all(), write_only=True,
    )

    class Meta:
        model = UserHabit
        fields = ['id', 'user', 'habit', 'habit_id', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def create(self, validated_data):
        return UserHabit.objects.create(user=self.context['request'].user, **validated_data)

    def update(self, instance, validated_data):
        instance.habit = validated_data.get('habit', instance.habit)
        instance.save(update_fields=['habit', 'updated_at'])
        return instance
