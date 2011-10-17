"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import words


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class wordsTest(TestCase):
    def setUp(self):
        words.objects.create(word="testCaseNow")
        pass       
    def tearDown(self):
        words.objects.get(word="testCaseNow").delete()
        
    def testAddWords(self):
        self.assertEquals(words.objects.filter(word="testCaseNow").count(), 1)