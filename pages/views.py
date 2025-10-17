from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .forms import Loginform
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def about(request):
    x=request.POST.get('username')
    y=request.POST.get('password')
    data = Login(username=x, password=y)
    # data.save()
    return render(request, 'pages/about.html',{'lf':Loginform})