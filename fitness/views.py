from django.shortcuts import render
from .models import Day, Workout, Exercise, Meal
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'fitness/home.html')

def day_list(request):
    days = Day.objects.all().order_by('-date')
    return render(request, 'fitness/day_list.html', {'days': days})

class DayListView(LoginRequiredMixin, ListView):
    model = Day
    template_name = 'fitness/day_list.html'
    context_object_name = 'days'
    ordering = ['-date']

    def get_queryset(self):
        return Day.objects.filter(user = self.request.user).order_by('date')

class DayDetailView(LoginRequiredMixin, DetailView):
    model = Day
    template_name = 'fitness/day_detail.html'

    def get_queryset(self):
        return Day.objects.filter(user =self.request.user)

class DayCreateView(LoginRequiredMixin, CreateView):
    model = Day
    fields = ['date', 'bodyweight']
    template_name = 'fitness/day_form.html'
    success_url = reverse_lazy('day_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DayUpdateView(LoginRequiredMixin, UpdateView):
    model = Day
    fields = ['date', 'bodyweight']
    template_name = 'fitness/day_form.html'
    success_url = reverse_lazy('day_list')

    def get_queryset(self):
        return Day.objects.filter(user=self.request.user)

class DayDeleteView(LoginRequiredMixin, DeleteView):
    model = Day
    template_name = 'fitness/day_confirm_delete.html'
    success_url = reverse_lazy('day_list')

    def get_queryset(self):
        return Day.objects.filter(user=self.request.user)

class WorkoutListView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = 'fitness/workout_list.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        return Workout.objects.filter(day__user = self.request.user)

class WorkoutDetailView(LoginRequiredMixin, DetailView):
    model = Workout
    template_name = 'fitness/workout_detail.html'

    def get_queryset(self):
        return Workout.objects.filter(day__user = self.request.user)

class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['day']
    template_name = 'fitness/workout_form.html'
    success_url = reverse_lazy('workout_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['day'].queryset = Day.objects.filter(user=self.request.user)
        return form

class WorkoutUpdateView(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ['day']
    template_name = 'fitness/workout_form.html'
    success_url = reverse_lazy('workout_list')

    def get_queryset(self):
        return Workout.objects.filter(day__user=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['day'].queryset = Day.objects.filter(user=self.request.user)
        return form

class WorkoutDeleteView(LoginRequiredMixin, DeleteView):
    model = Workout
    template_name = 'fitness/workout_confirm_delete.html'
    success_url = reverse_lazy('workout_list')

    def get_queryset(self):
        return Workout.objects.filter(day__user=self.request.user)

class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'fitness/exercise_list.html'
    context_object_name = 'exercises'

    def get_queryset(self):
        return Exercise.objects.filter(workout__day__user=self.request.user)

class ExerciseDetailView(LoginRequiredMixin, DetailView):
    model = Exercise
    template_name = 'fitness/exercise_detail.html'

    def get_queryset(self):
        return Exercise.objects.filter(workout__day__user=self.request.user)

class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise 
    fields = ['workout', 'name', 'weight', 'reps', 'sets']
    template_name = 'fitness/exercise_form.html'
    success_url = reverse_lazy('exercise_list')

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        form.fields['workout'].queryset = Workout.objects.filter(day__user=self.request.user)
        return form

class ExerciseUpdateView(LoginRequiredMixin, UpdateView):
    model = Exercise
    fields = ['workout', 'name', 'weight', 'reps', 'sets']
    template_name = 'fitness/exercise_form.html'
    success_url = reverse_lazy('exercise_list')

    def get_queryset(self):
        return Exercise.objects.filter(workout__day__user=self.request.user)

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        form.fields['workout'].queryset = Workout.objects.filter(day__user=self.request.user)
        return form
    
class ExerciseDeleteView(LoginRequiredMixin, DeleteView):
    model = Exercise
    template_name = 'fitness/exercise_confirm_delete.html'
    success_url = reverse_lazy('exercise_list')

    def get_queryset(self):
        return Exercise.objects.filter(workout__day__user=self.request.user)

class MealListView(LoginRequiredMixin, ListView):
    model = Meal
    template_name = 'fitness/meal_list.html'
    context_object_name = 'meals'

    def get_queryset(self):
        return Meal.objects.filter(day__user=self.request.user)

class MealDetailView(LoginRequiredMixin, DetailView):
    model = Meal
    template_name = 'fitness/meal_detail.html'

    def get_queryset(self):
        return Meal.objects.filter(day__user=self.request.user)

class MealCreateView(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ['day', 'name', 'calories', 'carbs', 'protein', 'fat']
    template_name = 'fitness/meal_form.html'
    success_url = reverse_lazy('meal_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['day'].queryset = Day.objects.filter(user=self.request.user)
        return form
    
class MealUpdateView(LoginRequiredMixin, UpdateView):
    model = Meal
    fields = ['day', 'name', 'calories', 'carbs', 'protein', 'fat']
    template_name = 'fitness/meal_form.html'
    success_url = reverse_lazy('meal_list')

    def get_queryset(self):
        return Meal.objects.filter(day__user=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['day'].queryset = Day.objects.filter(user=self.request.user)
        return form
    
class MealDeleteView(LoginRequiredMixin, DeleteView):
    model = Meal
    template_name = 'fitness/meal_confirm_delete.html'
    success_url = reverse_lazy('meal_list')

    def get_queryset(self):
        return Meal.objects.filter(day__user=self.request.user)


