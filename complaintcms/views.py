from django.shortcuts import render
from .forms import UploadFileForm
from .models import Complaint

# Create your views here.
def index(request):
    return render(request, 'complaintcms/index.html')

def result(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES.getlist('file')
        complaint = Complaint.objects.create(cszl_mp3 = file)
        complaint.save()
    else:
        form = UploadFileForm()
    return render(request, 'complaintcms/result.html',{'form':form})