from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question_en="What is Python?",
            answer_en="<p>A programming language.</p>"
        )

    def test_faq_translation(self):
        response = self.client.get('/api/faqs/?lang=hi')
        self.assertEqual(response.status_code, 200)
        self.assertIn('question', response.data[0])