from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Complaint
import datetime,re

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
    if request.method == 'POST':
        rawdata = request.POST['rawdata']
        new_list = rawdata.split(' ')
        
        jb_date = new_list[21].strip() + ' ' + new_list[22].strip()
        rk_date = new_list[24].strip() + ' ' + new_list[25].strip()
        ld_date = new_list[27].strip() + ' ' +new_list[28].strip()
        # print(jb_date)
        # print(rk_date)
        # print(ld_date)
        datasrc = {
            'tousuid':new_list[1],
            'lyqd':new_list[3],
            'jbhm':new_list[5],
            'jbhmyys':new_list[9],
            'jbhmgssf':new_list[13],
            'jbhmgscs':new_list[17],
            'bjbhm':new_list[7],
            'bjbhmgssf':new_list[15],
            'bjbhmgscs':new_list[19],
            'jb_date':datetime.datetime.strptime(jb_date,"%Y-%m-%d %H:%M:%S"),
            'ld_date':datetime.datetime.strptime(ld_date,"%Y-%m-%d %H:%M:%S"),
            'thsc':new_list[32],
            'bllx':new_list[30],
            'bjbhmlx':new_list[34],
            'jbnr':new_list[36],
            'rk_date':datetime.datetime.strptime(rk_date,"%Y-%m-%d %H:%M:%S"),
            'is_br':True,
            'is_cszl':False,
            'is_tjyd':False
        }

        print(datasrc)
        # obj,created = Complaint.objects.update_or_create(
        #     tousuid = context['tousuid'],
        #     defaults=context[1:]
        # )
    # obj,created = Complaint.objects.update_or_create(
    #     tousuid = new_list[1],
    #     defaults={
    #         'lyqd':new_list[3],
    #         'jbhm':new_list[5],
    #         'jbhmyys':new_list[9],
    #         'jbhmgssf':new_list[13],
    #         'jbhmgscs':new_list[17],
    #         'bjbhm':new_list[7],
    #         'bjbhmgssf':new_list[15],
    #         'bjbhmgscs':new_list[19],
    #         'jb_date':datetime.datetime.strptime(jb_date,"%Y/%m/%d %H:%M:%S"),
    #         'ld_date':datetime.datetime.strptime(ld_date,"%Y/%m/%d %H:%M:%S"),
    #         'thsc':new_list[32],
    #         'bllx':new_list[30],
    #         'bjbhmlx':new_list[34],
    #         'jbnr':new_list[36],
    #         'rk_date':datetime.datetime.strptime(rk_date,"%Y/%m/%d %H:%M:%S"),
    #         'is_br':True,
    #         'is_cszl':False,
    #         'is_tjyd':False

    #     }
    # )

    # Complaint.objects.get(tousuid=request.POST[''])
        return render(request,'complaintcms/saveto.html',datasrc)
    return render(request,'complaintcms/parse.html')
def saveto(request):
    pass
    # return render(request,'complaintcms/saveto.html')
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