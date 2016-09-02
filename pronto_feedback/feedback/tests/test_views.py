from django.core.urlresolvers import reverse
from django.test import TestCase

from taggit.models import Tag

from ..models import Feedback


class FeedbackViewTest(TestCase):
    def setUp(self):
        self.url = reverse('feedback')

    def test_access_feedback_index_page(self):
        response = self.client.get(self.url)

        expected = '<h1>Feedback</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_feedback_page_should_have_upload_form(self):
        response = self.client.get(self.url)

        expected = '<form action="." method="post" '
        expected += 'enctype="multipart/form-data">'
        self.assertContains(response, expected, status_code=200)
        expected = "<input type='hidden' name='csrfmiddlewaretoken'"
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
