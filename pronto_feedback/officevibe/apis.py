import requests


class OfficeVibeManager(object):
    def __init__(self):
        self.feedback_url = 'https://app.officevibe.com/api/v2/feedback'

    def get_feedback(self):
        requests.get(self.feedback_url)
