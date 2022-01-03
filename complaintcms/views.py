from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Complaint

# Create your views here.
def index(request):
    return render(request, 'complaintcms/index.html')

def result(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            tousuid = form.data.get('tousuid')
            csjg = form.data.get('csjg')
            bcsr = form.data.get('bcsr')
            yqje = form.data.get('yqje')
            yqts = form.data.get('yqts')
            is_br = form.data.get('is_br')
            cszl_img1 = form.files.get('cszl_img1')
            cszl_img2 = form.files.get('cszl_img2')
            cszl_img3 = form.files.get('cszl_img3')
            cszl_mp3 = form.files.get('cszl_mp3')
            obj,updated = Complaint.objects.update_or_create(
                tousuid = tousuid,
                defaults={
                    'csjg':csjg,
                    'bcsr':bcsr,
                    'yqje':yqje,
                    'yqts':yqts,
                    'is_br':is_br,
                    'cszl_img1':cszl_img1,
                    'cszl_img2':cszl_img2,
                    'cszl_img3':cszl_img3,
                    'cszl_mp3':cszl_mp3
                }
            )
        context = {
            'obj':obj,
            'updated':updated,
        }
    return render(request,'complaintcms/result.html',context)

def parse(request):
    return render(request,'complaintcms/parse.html')