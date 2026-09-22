from django.shortcuts import render
from .models import Day, Workout, Exercise, Meal
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    return render(request, 'fitness/home.html')

def day_list(request):
    days = Day.objects.all().order_by('-date')
    return render(request, 'fitness/day_list.html', {'days': days})

class DayListView(ListView):
    model = Day
    template_name = 'fitness/day_list.html'
    context_object_name = 'days'
    ordering = ['-date']
    def get_queryset(self):
        return Day.objects.filter(user = self.request.user).order_by('date')

class DayDetailView(DetailView):
    model = Day
    template_name = 'fitness/day_detail.html'

class DayCreateView(CreateView):
    model = Day
    fields = ['date', 'bodyweight']
    template_name = 'fitness/day_form.html'
    success_url = reverse_lazy('day_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DayUpdateView(UpdateView):
    model = Day
    fields = ['date', 'bodyweight']
    template_name = 'fitness/day_form.html'
    success_url = reverse_lazy('day_list')

class DayDeleteView(DeleteView):
    model = Day
    template_name = 'fitness/day_confirm_delete.html'
    success_url = reverse_lazy('day_list')

class WorkoutListView(ListView):
    model = Workout
    template_name = 'fitness/workout_list.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        return Workout.objects.filter(day__user = self.request.user)

class WorkoutDetailView(DetailView):
    model = Workout
    template_name = 'fitness/workout_detail.html'

class WorkoutCreateView(CreateView):
    model = Workout
    fields = ['day']
    template_name = 'fitness/workout_form.html'
    success_url = reverse_lazy('workout_list')

class WorkoutUpdateView(UpdateView):
    model = Workout
    fields = ['day']
    template_name = 'fitness/workout_form.html'
    success_url = reverse_lazy('workout_list')

class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = 'fitness/workout_confirm_delete.html'
    success_url = reverse_lazy('workout_list')

class ExerciseListView(ListView):
    model = Exercise
    template_name = 'fitness/exercise_list.html'
    context_object_name = 'exercises'

    def get_queryset(self):
        return Exercise.objects.filter(workout__day__user=self.request.user)

class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = 'fitness/exercise_detail.html'

class ExerciseCreateView(CreateView):
    model = Exercise 
    fields = ['workout', 'name', 'weight', 'reps', 'sets']
    template_name = 'fitness/exercise_form.html'
    success_url = reverse_lazy('exercise_list')

class ExerciseUpdateView(UpdateView):
    model = Exercise
    fields = ['workout', 'name', 'weight', 'reps', 'sets']
    template_name = 'fitness/exercise_form.html'
    success_url = reverse_lazy('exercise_list')

class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = 'fitness/exercise_confirm_delete.html'
    success_url = reverse_lazy('exercise_list')

class MealListView(ListView):
    model = Meal
    template_name = 'fitness/meal_list.html'
    context_object_name = 'meals'

    def get_queryset(self):
        return Meal.objects.filter(day__user=self.request.user)

class MealDetailView(DetailView):
    model = Meal
    template_name = 'fitness/meal_detail.html'

class MealCreateView(CreateView):
    model = Meal
    fields = ['day', 'name', 'calories', 'carbs', 'protein', 'fat']
    template_name = 'fitness/meal_form.html'
    success_url = reverse_lazy('meal_list')

class MealUpdateView(UpdateView):
    model = Meal
    fields = ['day', 'name', 'calories', 'carbs', 'protein', 'fat']
    template_name = 'fitness/meal_form.html'
    success_url = reverse_lazy('meal_list')

class MealDeleteView(DeleteView):
    model = Meal
    template_name = 'fitness/meal_confirm_delete.html'
    success_url = reverse_lazy('meal_list')


