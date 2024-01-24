from django.test import TestCase,SimpleTestCase
from django.urls import reverse
# Create your tests here.

class HomePageViewTest(SimpleTestCase):
    def test_url_exists(self):
        respone=self.client.get("/")
        self.assertEqual(respone.status_code,200)

    def test_homepage_view(self):
        respone=self.client.get(reverse('home'))
        self.assertEqual(respone.status_code,200)
        self.assertTemplateUsed(respone,"home.html")
        self.assertContains(respone,"Home")