import os


def handle_uploaded_file(f):
    with open(os.path.join(os.getcwd(), 'uploader', 'static', 'upload', f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return os.path.join(os.getcwd(), 'uploader', 'static', 'upload', f.name)
