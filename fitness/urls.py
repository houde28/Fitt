from django.urls import path
from . import views

urlpatterns = [
    path('days/', views.DayListView.as_view(), name='day_list'),
    path('days/<int:pk>/', views.DayDetailView.as_view(), name = 'day_detail'),
    path('days/new/', views.DayCreateView.as_view(), name = 'day_create'),
    path('days/<int:pk>/edit/',views.DayUpdateView.as_view(), name= 'day_update'),
    path('days/<int:pk>/delete/', views.DayDeleteView.as_view(), name = 'day_delete'),

    path('workouts/', views.WorkoutListView.as_view(), name='workout_list'),
    path('workouts/<int:pk>/', views.WorkoutDetailView.as_view(), name='workout_detail'),
    path('workouts/new/',views.WorkoutCreateView.as_view(), name='workout_create'),
    path('workouts/<int:pk>/edit/', views.WorkoutUpdateView.as_view(), name = 'workout_update'),
    path('workouts/<int:pk>/delete/', views.WorkoutDeleteView.as_view(), name='workout_delete'),

    path('exercises/', views.ExerciseListView.as_view(), name ='exercise_list'),
    path('exercises/<int:pk>/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
    path('exercises/new/', views.ExerciseCreateView.as_view(), name = 'exercise_create'),
    path('exercises/<int:pk>/edit/', views.ExerciseUpdateView.as_view(), name = 'exercise_update'),
    path('exercises/<int:pk/delete/', views.ExerciseDeleteView.as_view(), name = 'exercise_delete'),

    path('meals/', views.MealListView.as_view(), name= 'meal_list'),
    path('meals/<int:pk>/', views.MealDetailView.as_view(), name = 'meal_detail'),
    path('meals/new/', views.MealCreateView.as_view(), name = 'meal_create'),
    path('meals/<int:pk>/edit/', views.MealUpdateView.as_view(), name = 'meal_update'),
    path('meals/<int:pk/delete', views.MealDeleteView.as_view(), name = 'meal_delete'),
]