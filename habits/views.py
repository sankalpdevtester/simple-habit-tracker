from rest_framework import generics
from .models import Habit, HabitLog, HabitCategory
from .serializers import HabitSerializer, HabitLogSerializer, HabitCategorySerializer
from rest_framework.permissions import IsAuthenticated

class HabitCategoryList(generics.ListCreateAPIView):
    queryset = HabitCategory.objects.all()
    serializer_class = HabitCategorySerializer
    permission_classes = [IsAuthenticated]

class HabitList(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user).select_related('category')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HabitLogList(generics.ListCreateAPIView):
    serializer_class = HabitLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HabitLog.objects.filter(habit__user=self.request.user).select_related('habit', 'habit__category')
