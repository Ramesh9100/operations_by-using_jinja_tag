from django.shortcuts import render

# Create your views here.

def Ram(request):
    d={'a':1000,'b':5000,'c':3000}
    return render(request,'Ram.html',d)