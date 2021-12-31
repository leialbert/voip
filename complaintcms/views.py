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
            cszl_img = form.files.get('cszl_img')
            cszl_mp3 = form.files.get('cszl_mp3')
            # print(tousuid)
            # print(csjg)
            # print(bcsr)
            # print(yqje)
            # print(yqts)
            # print(is_br)
            # print(cszl_img)
            # print(cszl_mp3)
            Complaint.objects.update_or_create(
                tousuid = tousuid,
                defaults={
                    'csjg':csjg,
                    'bcsr':bcsr,
                    'yqje':yqje,
                    'yqts':yqts,
                    'is_br':is_br,
                    'cszl_img':cszl_img,
                    'cszl_mp3':cszl_mp3
                }
            )

    return HttpResponse('sucess')

def parse(request):
    return render(request,'complaintcms/parse.html')