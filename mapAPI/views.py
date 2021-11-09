from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def location(request):
    return render(request, 'location.html')

def jusoPopup(request):
    return render(request, 'jusoPopup.html')

def keyword(request):
    return render(request, 'keyword.html')

def category(request):
    return render(request, 'category.html')

def clickmarker(request):
    return render(request, 'clickmarker.html')