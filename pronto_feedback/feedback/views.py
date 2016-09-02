from datetime import datetime

from django.shortcuts import render
from django.utils import timezone
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

    def post(self, request):
        data = request.FILES['file_upload'].readlines()[1:]
        for each in data:
            each = each.split(',')
            creation_date = datetime.strptime(
                each[2],
                '%m/%d/%Y %H:%M'
            ).replace(tzinfo=timezone.utc)
            Feedback.objects.create(
                fid=each[0],
                creation_date=creation_date,
                question_asked=each[4],
                message=each[5]
            )

        return render(
            request,
            self.template_name
        )
