from django.shortcuts import render

# Create your views here.
def hel(request):
    return render(request,'hello.html')