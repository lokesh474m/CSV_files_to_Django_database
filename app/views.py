from django.shortcuts import render

from app.models import *

import csv

from django.http import HttpResponse
# Create your views here.

def insert_bank(request):
    with open('C:\\Users\lenovo\\OneDrive\\Desktop\\django projects\\lokesh\\Scripts\\project35\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()
            BOD=Bank.objects.all()
            d={'BOD':BOD}
    return render(request,'Bank_details.html',d)

def insert_branch(request):
    with open('C:\\Users\\lenovo\\OneDrive\\Desktop\\django projects\\lokesh\\Scripts\\project35\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=i[1]
                br=i[2]
                add=i[3]
                con=i[4]
                cit=i[5]
                dt=i[6]
                st=i[7]
                BRO=Branch(bank_name=BO[0],ifsc=ifs,branch=br,address=add,contact=con,city=cit,district=dt,state=st)
                BRO.save()
                BRO=Branch.objects.all()
            d={'BRO':BRO}
    return render(request,'Details_of_bank.html',d)

