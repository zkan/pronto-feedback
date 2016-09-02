from datetime import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

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

    def test_feedback_page_should_save_data_from_uploaded_csv_file(self):
        file_upload = open('tests/test_data.csv', 'rb')
        data = {
            'file_upload': file_upload
        }

        self.client.post(self.url, data=data)

        feedback = Feedback.objects.latest('id')
        self.assertEqual(feedback.fid, '57bd22d66706c30f00ad7xxx')
        creation_date = datetime(2016, 8, 24, 11, 30, 0, tzinfo=timezone.utc)
        self.assertEqual(feedback.creation_date, creation_date)
        self.assertEqual(feedback.question_asked, "What's on your mind?")
        self.assertEqual(feedback.message, 'I like frozen blueberries!')
