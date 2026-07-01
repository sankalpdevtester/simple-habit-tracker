from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from habits.models import UserHabit
from habits.serializers import UserHabitSerializer
from habits.permissions import IsAuthenticated

class UserHabitView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_habits = UserHabit.objects.filter(user=request.user)
        serializer = UserHabitSerializer(user_habits, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserHabitSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserHabitDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            user_habit = UserHabit.objects.get(pk=pk, user=request.user)
            serializer = UserHabitSerializer(user_habit)
            return Response(serializer.data)
        except UserHabit.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            user_habit = UserHabit.objects.get(pk=pk, user=request.user)
            serializer = UserHabitSerializer(user_habit, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserHabit.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            user_habit = UserHabit.objects.get(pk=pk, user=request.user)
            user_habit.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserHabit.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)