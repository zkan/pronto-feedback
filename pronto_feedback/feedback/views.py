import csv
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

    def save_feedback(self, data):
        creation_date = datetime.strptime(
            data[2],
            '%m/%d/%Y %H:%M'
        ).replace(tzinfo=timezone.utc)

        Feedback.objects.create(
            fid=data[0],
            creation_date=creation_date,
            question_asked=data[4],
            message=data[5]
        )

    def post(self, request):
        feedback = Feedback.objects.all()

        form = FeedbackUploadForm(request.POST, request.FILES)

        if form.is_valid():
            reader = csv.reader(request.FILES['file_upload'])
            reader.next()
            map(self.save_feedback, reader)

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'feedback': feedback
            }
        )
