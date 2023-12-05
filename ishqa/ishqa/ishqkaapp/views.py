from django.shortcuts import render
from django.shortcuts import render, redirect
from ishqkaapp.forms import RequestCreate
from django.contrib import messages
from ishqkaapp.models import Request,Approved,Booking
# Create your views here.

def request(request):
    if request.method == "POST":
        form = RequestCreate(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = RequestCreate()
    return render(request,'request.html',{'form':form})

def home(request):
    employees = Request.objects.all()
    return render(request, "home.html", {'employees': employees})

def approved(request,id):
    form =  Request.objects.get(id=id)
    fm=Approved.objects.all()
    return render(request, 'approved.html', {'form':form ,'fm':fm})
def save(request):
    if request.method == "POST":
        ap=Approved()
        ap.request = request.POST['request']
        ap.approved_at = request.POST['approved_at']
        ap.save()
        messages.success(request, "Registration Successfull")

    return render(request, "home.html")
