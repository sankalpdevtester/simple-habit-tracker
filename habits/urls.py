from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.HabitCategoryList.as_view()),
    path('habits/', views.HabitList.as_view()),
    path('logs/', views.HabitLogList.as_view()),
]