import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django import forms
from django.utils import timezone
from django.test import TestCase

from taggit.models import Tag

from .forms import FeedbackUploadForm
from .models import Feedback


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


class FeedbackViewTest(TestCase):
    def setUp(self):
        self.url = reverse('feedback')

    def test_access_feedback_index_page(self):
        response = self.client.get(self.url)

        expected = '<h1>Feedback</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_feedback_page_should_have_upload_form(self):
        response = self.client.get(self.url)

        expected = '<form action="." method="post">'
        self.assertContains(response, expected, status_code=200)
        expected = '<label for="file_upload">Select CSV File:</label>'
        self.assertContains(response, expected, status_code=200)
        expected = '<input class="form-control" id="id_file_upload" '
        expected += 'name="file_upload" type="file" required />'
        self.assertContains(response, expected, status_code=200)

    def test_feedback_page_should_have_feedback_table(self):
        response = self.client.get(self.url)

        expected = '<th width="20%">Feedback ID</th>'
        expected += '<th>Question Asked</th>'
        expected += '<th>Message</th>'
        expected += '<th width="20%">Tags</th>'
        self.assertContains(response, expected, status_code=200)

    def test_feedback_page_should_show_feedback_data(self):
        feedback = Feedback.objects.create(
            fid='57504457a6cca38a00cfb4f88',
            question_asked='How are you today?',
            message="I'm happy",
        )
        suggestion_box_tag = Tag.objects.create(name='Suggestion Box')
        good_tag = Tag.objects.create(name='good')
        feedback.tags.add(suggestion_box_tag)
        feedback.tags.add(good_tag)

        response = self.client.get(self.url)

        expected = '<td>57504457a6cca38a00cfb4f88</td>'
        expected += '<td>How are you today?</td>'
        expected += '<td>I&#39;m happy</td>'
        expected += '<td><span class="label label-info">Suggestion Box</span>'
        expected += '&nbsp;<span class="label label-info">good</span>&nbsp;'
        self.assertContains(response, expected, status_code=200)


class FeedbackUploadFormTest(TestCase):
    def setUp(self):
        self.form = FeedbackUploadForm()

    def test_feedback_upload_form_should_have_all_defined_fields(self):
        expected_fields = [
            'file_upload'
        ]
        for each in expected_fields:
            self.assertTrue(each in self.form.fields)

        self.assertEqual(len(self.form.fields), 1)

    def test_feedback_upload_form_should_file_field(self):
        self.assertIsInstance(
            self.form.fields['file_upload'],
            forms.fields.FileField
        )

    def test_form_should_use_file_input_widget_with_form_control_class(self):
        self.assertIsInstance(
            self.form.fields['file_upload'].widget,
            forms.FileInput
        )

        self.assertEqual(
            self.form.fields['file_upload'].widget.attrs,
            {'class': 'form-control'}
        )


class FeedbackAdminTest(TestCase):
    def test_access_feedback_admin(self):
        User.objects.create_superuser('admin', 'admin@pronto.com', 'admin')
        self.client.login(username='admin', password='admin')

        url = '/admin/feedback/feedback/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
