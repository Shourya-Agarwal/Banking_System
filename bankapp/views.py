from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from bankapp.models import Customers, transactions
# Create your views here.
def index(request):
    return render(request,'home.html')
    # return HttpResponse("this is home")
def customers(request):
    data=Customers.objects.all()
    # print(data)
    # d1=Customers.objects.filter(name="Aman Kumar").update(value=)
    return render(request, 'customers.html',{"messages":data})
    # return HttpResponse("this is customer transaction detials page")
def history(request):
    tran_data=transactions.objects.all()
    return render(request, 'history.html',{"tran_messages":tran_data})

def transaction(request):
    # Data comes from customer table's anchor tage
    t=request.GET.get('data')
    x,y=t.split("?")
    data=Customers.objects.all()
    return render(request,'transaction.html',{"name_from":x,"amt":y,"messages":data})

def update_info(request):
    t=request.GET.get('data')
    if request.method=="POST":
        tranfer_amt=request.POST.get('amt')
        naam=request.POST.get('transfer_to')
        x=Customers.objects.get(id=naam)
        y=Customers.objects.get(name=t)
        x.credits=x.credits+int(tranfer_amt)
        y.credits=y.credits-int(tranfer_amt)
        x.save()
        y.save()
        z=transactions(from1=y,to1=x,amount=tranfer_amt)
        z.save()
        return render(request,'history.html',{"name":x,"from":y,"paisa":tranfer_amt})
        # update_table=Customers()
    
def this(request):
    data=transactions.objects.all().order_by('-id')
    return render(request, 'this.html',{"messages":data})
    
