from django.test import TestCase

from ..models import Metric


class MetricTest(TestCase):
    def test_save_metric_should_have_data_in_each_defined_field(self):
        metric = Metric()
        metric.name = 'Relationship with colleagues'
        metric.save()

        metric = Metric.objects.latest('id')

        self.assertEqual(metric.name, 'Relationship with colleagues')
