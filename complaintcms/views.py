from django.shortcuts import render
from .forms import UploadFileForm
from .models import Complaint

# Create your views here.
def index(request):
    return render(request, 'complaintcms/index.html')

def result(request):
    if request.method == 'POST':
        rawdata = request.POST['rawdata']
        rawlist = rawdata.split()
    return render(request, 'complaintcms/result.html',{'rawdata':rawlist})

def parse(request):
    return render(request,'complaintcms/parse.html')