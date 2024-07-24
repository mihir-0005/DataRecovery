from django.shortcuts import render
from django.http import FileResponse, Http404
import os
from django.conf import settings

def index(request):
    return render(request, 'myapp/index.html')

def download_zip(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'files', 'myfile.zip')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='myfile.zip')
    else:
        raise Http404("File not found")
