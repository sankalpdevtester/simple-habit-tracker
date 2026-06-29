from rest_framework import generics
from .models import Habit, HabitLog, HabitCategory
from .serializers import HabitSerializer, HabitLogSerializer, HabitCategorySerializer
from rest_framework.permissions import IsAuthenticated

class HabitCategoryList(generics.ListCreateAPIView):
    queryset = HabitCategory.objects.all()
    serializer_class = HabitCategorySerializer
    permission_classes = [IsAuthenticated]

class HabitList(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

class HabitLogList(generics.ListCreateAPIView):
    queryset = HabitLog.objects.all()
    serializer_class = HabitLogSerializer
    permission_classes = [IsAuthenticated]