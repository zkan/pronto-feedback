from django.contrib.auth.models import User
from django.test import TestCase


class FeedbackAdminTest(TestCase):
    def test_access_feedback_admin(self):
        User.objects.create_superuser('admin', 'admin@pronto.com', 'admin')
        self.client.login(username='admin', password='admin')

        url = '/admin/feedback/feedback/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
