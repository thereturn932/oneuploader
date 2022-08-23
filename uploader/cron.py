from .models import File
from django.conf import settings
from datetime import datetime, timedelta


def clean_old_files():
    treshold = datetime.now() - timedelta(hours=24)
    objects = File.objects.filter(created_at__lte=treshold)
    for obj in objects:
        print(obj.file_directory)
