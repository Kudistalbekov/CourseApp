from django.test import SimpleTestCase
from django.urls import reverse,resolve
from myApp.views import * 
class UrlsTestClass(SimpleTestCase):
        
        def test_list(self):
            url = reverse('list')
            self.assertEquals(resolve(url).func.view_class,CourseAPI)