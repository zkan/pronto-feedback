from django.test import TestCase

from .models import Feedback


class FeedbackTest(TestCase):
    def test_save_feedback_should_have_message(self):
        feedback = Feedback()
        feedback.message = "I'm happy"
        feedback.save()

        feedback = Feedback.objects.latest('id')

        self.assertEqual(feedback.message, "I'm happy")
