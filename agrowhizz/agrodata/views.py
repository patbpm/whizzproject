from django.shortcuts import render
from .models import Database
from django.contrib.auth.decorators import login_required
# Create your views here.
def agrodata(request):
    
    return render(request, 'agrodata/agrodata.html', {})

@login_required
def foodindustrydata(request):
    databases = Database.objects.all()
    context = {
        'databases': databases,  
    }
    return render(request, 'agrodata/foodindustrydata.html', context)