from django.shortcuts import render

# Create your views here.

# views for the Home Page.
def homePage(request):
    return render(request, 'home/homePage.html', {})

# views for the WhatWedo Page.
def whatWeDo(request):
    return render(request, 'home/whatWeDo.html', {})

# views for the whatWeServe Page.
def whatWeServe(request):
    return render(request, 'home/asideLayout.html', {})
