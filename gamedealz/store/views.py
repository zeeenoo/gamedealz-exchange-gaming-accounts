from django.shortcuts import render

# Create your views here

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'store/about.html')

def contact(request):
    return render(request,'store/contact.html')

def tracker(request):
    return render(request,'store/tracker.html')
