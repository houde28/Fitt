from django.db import models
from django.contrib.auth.models import User

class Day(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    bodyweight = models.DecimalField(max_digits = 5, decimal_places=2, null = True, blank = True)

class Workout(models.Model):
    day =  models.ForeignKey(Day, on_delete=models.CASCADE, related_name='workouts')

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    reps = models.PositiveSmallIntegerField()
    sets = models.PositiveSmallIntegerField()

class Meal(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name= 'meals')
    name = models.CharField(max_length=100)
    calories = models.PositiveSmallIntegerField()
    carbs = models.PositiveSmallIntegerField()
    protein = models.PositiveSmallIntegerField()
    fat = models.PositiveSmallIntegerField()


