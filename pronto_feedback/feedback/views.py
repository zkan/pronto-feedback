from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import FeedbackUploadForm
from .models import Feedback


class FeedbackView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        feedback = Feedback.objects.all()

        form = FeedbackUploadForm()

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'feedback': feedback
            }
        )
