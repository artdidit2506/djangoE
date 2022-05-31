from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/index.html')
def logo(request):
    return render(request, 'base/logo.html')
