from rest_framework import serializers
from habits.models import UserHabit
from habits.serializers import HabitSerializer

class UserHabitSerializer(serializers.ModelSerializer):
    habit = HabitSerializer(read_only=True)

    class Meta:
        model = UserHabit
        fields = ['id', 'user', 'habit', 'created_at', 'updated_at']

    def create(self, validated_data):
        user_habit = UserHabit.objects.create(
            user=self.context['request'].user,
            habit=validated_data['habit']
        )
        return user_habit

    def update(self, instance, validated_data):
        instance.habit = validated_data.get('habit', instance.habit)
        instance.save()
        return instance