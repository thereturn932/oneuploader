from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from .models import File
from .forms import UploadForm
from .functions import handle_uploaded_file
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
import os
# Create your views here.


def index(request):
    if request.method == 'POST':
        file = UploadForm(request.POST, request.FILES)
        if(File.objects.filter(unique_id=request.POST['unique_id']).exists()):
            messages.info(request, "Unique Id already exists")
            return redirect('index')
        elif (os.path.exists(os.path.join(os.getcwd(), 'uploader', 'static', 'upload', request.FILES['file_directory'].name))):
            messages.info(request, "File with the same name already exists")
            return redirect('index')
        else:
            if file.is_valid():
                dest = handle_uploaded_file(request.FILES['file_directory'])
                file_model = File(
                    unique_id=request.POST['unique_id'], file_directory=dest)
                file_model.save()
                messages.info(
                    request, "File uploaded successfuly")
                return redirect('index')
    else:
        file = UploadForm()
        return render(request, "index.html", {'form': file})


def upload(request):
    if request.method == 'POST':
        file = UploadForm(request.POST, request.FILES)
        if(File.objects.filter(unique_id=request.POST['unique_id']).exists()):
            messages.info(request, "Unique Id already exists")
            return redirect('index')
        elif (os.path.exists(os.path.join(os.getcwd(), 'uploader', 'static', 'upload', request.FILES['file_directory']))):
            messages.info(request, "File with the same name already exists")
            return redirect('index')
        else:
            if file.is_valid():
                dest = handle_uploaded_file(request.FILES['file_directory'])
                file_model = File(
                    unique_id=request.POST['unique_id'], file_directory=dest)
                file_model.save()
                return HttpResponse("File uploaded successfuly")
    else:
        file = UploadForm()
        return render(request, "index.html", {'form': file})


def download(request):
    if request.method == 'POST':
        if not File.objects.filter(unique_id=request.POST['unique_id']).exists():
            messages.info(request, "Unique Id does not exist")
            return redirect('index')
        else:
            file = File.objects.get(unique_id=request.POST['unique_id'])
            file_path = file.file_directory
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(
                        fh.read(), content_type='application/force-download')
                    print(os.path.basename(file_path))
                    response[
                        'Content-Disposition'] = f'inline; filename={os.path.basename(file_path)}'
                    return response
    if request.method == 'GET':
        file = UploadForm()
        return render(request, "index.html", {'form': file})
