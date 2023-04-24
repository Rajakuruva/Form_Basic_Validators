from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def Student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SO=StudentForm(request.POST)
        if SO.is_valid():
            return HttpResponse(str(SO.cleaned_data))
        else:
            return HttpResponse("Give valid data!!!")
    return render(request,'Student.html',d)