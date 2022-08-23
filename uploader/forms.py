from django import forms


class UploadForm(forms.Form):
    unique_id = forms.CharField(max_length=100)
    file_directory = forms.FileField()
