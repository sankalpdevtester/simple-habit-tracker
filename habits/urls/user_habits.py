from django.urls import path
from habits.views import UserHabitView, UserHabitDetailView

urlpatterns = [
    path('user_habits/', UserHabitView.as_view()),
    path('user_habits/<int:pk>/', UserHabitDetailView.as_view()),
]