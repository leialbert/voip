from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Complaint
import datetime

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

def upload(request):
    with open('tszl.txt','r',encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            record = list(line.split('\t'))
            # print(record[9])
            
            obj,updated = Complaint.objects.update_or_create(
                tousuid = record[0],
                defaults={
                    'lyqd':record[1],
                    'jbhm':record[2],
                    'jbhmyys':record[3],
                    'jbhmgssf':record[4],
                    'jbhmgscs':record[5],
                    'bjbhm':record[6],
                    'bjbhmgssf':record[7],
                    'bjbhmgscs':record[8],
                    'jb_date':datetime.datetime.strptime(record[9],"%Y/%m/%d %H:%M"),
                    'ld_date':datetime.datetime.strptime(record[10],"%Y/%m/%d %H:%M"),
                    'thsc':record[11],
                    'bllx':record[12],
                    'bjbhmlx':record[13],
                    'jbnr':record[14],
                    'rk_date':datetime.datetime.strptime(record[15],"%Y/%m/%d %H:%M"),
                    'csms':record[16],
                    'is_br':True,
                    'is_cszl':True,
                    'is_tjyd':True

                }
            )
    return render(request,'complaintcms/parse.html')