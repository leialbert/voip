from django.shortcuts import render
from .forms import UploadFileForm

# Create your views here.
def index(request):
    return render(request, 'complaintcms/index.html')

def result(request):
    return render(request, 'complaintcms/result.html')