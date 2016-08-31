import datetime

from django.utils import timezone
from django.test import TestCase

from taggit.models import Tag

from ..models import Feedback


class FeedbackTest(TestCase):
    def test_save_feedback_should_have_data_in_each_defined_field(self):
        some_date = datetime.datetime(2015, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        tag = Tag.objects.create(name='Suggestion Box')

        feedback = Feedback()
        feedback.fid = '57504457a6cca38a00cfb4f88'
        feedback.creation_date = some_date
        feedback.last_modification_date = some_date
        feedback.question_asked = "What's on your mind?"
        feedback.message = "I'm happy"
        feedback.save()

        feedback = Feedback.objects.latest('id')
        feedback.tags.add(tag)

        self.assertEqual(feedback.fid, '57504457a6cca38a00cfb4f88')
        self.assertEqual(feedback.creation_date, some_date)
        self.assertEqual(feedback.last_modification_date, some_date)
        self.assertEqual(feedback.question_asked, "What's on your mind?")
        self.assertEqual(feedback.message, "I'm happy")
        self.assertEqual(feedback.tags.latest('id').name, 'Suggestion Box')
