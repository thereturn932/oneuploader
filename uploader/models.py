from django.db import models
from django.forms import ModelForm

# Create your models here.


class File(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)
    file_directory = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.unique_id


class UploadForm(ModelForm):
    class Meta:
        model = File
        fields = ['unique_id', 'file_directory']
