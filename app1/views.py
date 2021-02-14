from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
    return render(request,'h1.html')
def test(request):
    return render(request,'h2.html')
    

        