from django.test import TestCase
from django.contrib.auth.models import User
from .models import Day

class DaySecurityTest(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(username='usera',password='pass12345')
        self.user_b = User.objects.create_user(username='userb', password='pass12345')
        self.day_b = Day.objects.create(user=self.user_b, date='2026-01-01', bodyweight=150)

    def test_user_cannot_view_another_users_day(self):
        self.client.login(username='usera', password='pass12345')
        response = self.client.get(f'/days/{self.day_b.pk}/')
        self.assertEqual(response.status_code, 404)

    def test_user_can_view_their_own_day(self):
        self.client.login(username='userb',password='pass12345')
        response = self.client.get(f'/days/{self.day_b.pk}/')
        self.assertEqual(response.status_code,200)

    def test_logged_out_user_redirected_from_days(self):
        response =  self.client.get('/days/')
        self.assertEqual(response.status_code, 302)

class DayModelTest(TestCase):
    def test_day_str_return_date(self):
        user = User.objects.create_user(username='testuser', password='testpass123')
        day = Day.objects.create(user=user, date='2026-01-01', bodyweight=180)
        self.assertEqual(str(day), '2026-01-01')

    
