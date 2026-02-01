from django.test import TestCase, Client
from django.urls import reverse

class HealthCheckTest(TestCase):
    def test_health_check(self):
        client = Client()
        response = client.get(reverse('health'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

class ApiPostsTest(TestCase):
    def test_api_posts(self):
        client = Client()
        response = client.get(reverse('api_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])
