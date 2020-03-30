from django.test import TestCase, RequestFactory
from helloworld.views import HomePageView

class HelloWorldTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_home_page(self):
        request = self.factory.get('/')
        response = HomePageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'application/json')
        self.assertEqual(response.status_code, 200)
