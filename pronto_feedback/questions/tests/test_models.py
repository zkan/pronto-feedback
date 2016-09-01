from django.test import TestCase

from ..models import Question


class QuestionTest(TestCase):
    def test_save_question_should_have_data_in_each_defined_field(self):
        question = Question()
        question.title = "What's on your mind?"
        question.category = 'Questionnaire'
        question.save()

        question = Question.objects.latest('id')

        self.assertEqual(question.title, "What's on your mind?")
        self.assertEqual(question.category, 'Questionnaire')
