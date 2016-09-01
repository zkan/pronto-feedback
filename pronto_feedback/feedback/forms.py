from django import forms


class FeedbackUploadForm(forms.Form):
    file_upload = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
