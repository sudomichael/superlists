from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

class SmokeTest(TestCase):

    def test_bad_maths(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
