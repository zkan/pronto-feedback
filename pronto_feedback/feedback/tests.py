import datetime

from django.contrib.auth.models import User
from django.utils import timezone
from django.test import TestCase

from .models import Feedback


class FeedbackTest(TestCase):
    def test_save_feedback_should_have_data_in_each_defined_field(self):
        some_date = datetime.datetime(2015, 1, 1, 0, 0, 0, tzinfo=timezone.utc)

        feedback = Feedback()
        feedback.fid = '57504457a6cca38a00cfb4f88'
        feedback.creation_date = some_date
        feedback.last_modification_date = some_date
        feedback.question_asked = "What's on your mind?"
        feedback.message = "I'm happy"
        feedback.save()

        feedback = Feedback.objects.latest('id')

        self.assertEqual(feedback.fid, '57504457a6cca38a00cfb4f88')
        self.assertEqual(feedback.creation_date, some_date)
        self.assertEqual(feedback.last_modification_date, some_date)
        self.assertEqual(feedback.question_asked, "What's on your mind?")
        self.assertEqual(feedback.message, "I'm happy")


class FeedbackAdminTest(TestCase):
    def test_access_feedback_admin(self):
        User.objects.create_superuser('admin', 'admin@pronto.com', 'admin')
        self.client.login(username='admin', password='admin')

        url = '/admin/feedback/feedback/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
