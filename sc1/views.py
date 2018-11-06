from django.shortcuts import render
from .models import Sosio
# Create your views here.

def showIndex(request):
    return render(request,"index.html")

def displayDetails(request):
    no=request.POST.get("no")
    date=request.POST.get("date")
    amount=request.POST.get("amount")
    names=request.POST.getlist("h1")
    i=(",".join(names))
    noofpersons=len(names)
    print(noofpersons)
    total=int(amount)/noofpersons
    print(total)
    so=Sosio(no=no,date=date,amount=amount,names=i,res=total)
    so.save()
    d1={"No":no,"Date":date,"Amount":amount,"No of persons":i, "Indivisual Amount":total}

    return render(request,"index.html",{"ans":d1})


