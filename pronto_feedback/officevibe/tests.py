from mock import patch

from django.test import TestCase

from .apis import OfficeVibeManager


class OfficeVibeManagerTest(TestCase):
    @patch('officevibe.apis.requests.get')
    def test_get_feedback_should_call_officevibe_api(self, mock):
        manager = OfficeVibeManager()
        manager.get_feedback()
        mock.assert_called_once_with(
            'https://app.officevibe.com/api/v2/feedback'
        )
