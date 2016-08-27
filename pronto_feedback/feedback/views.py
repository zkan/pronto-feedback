from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Feedback


class FeedbackView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        feedback = Feedback.objects.all()

        return render(
            request,
            self.template_name,
            {
                'feedback': feedback
            }
        )
