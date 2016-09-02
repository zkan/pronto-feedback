from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from ..forms import FeedbackUploadForm


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

    def test_form_should_be_able_to_upload_file(self):
        upload_file = open('tests/test_data.csv', 'r')
        post_dict = {}
        file_dict = {
            'file_upload': SimpleUploadedFile(
                upload_file.name,
                upload_file.read()
            )
        }

        form = FeedbackUploadForm(post_dict, file_dict)

        self.assertTrue(form.is_valid())
