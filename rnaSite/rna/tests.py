from django.test import TestCase
from django.urls import resolve
from rna.views import home_page

'''
class SmokeTest(TestCase):
    """ mały test na sprawdzenie czy testowanie dziala (python manage.py test)
    """
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
'''

class HomePageTest(TestCase):
    """ weryfikacja strony glownej
    """
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
