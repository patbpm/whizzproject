from django.shortcuts import render
from .models import Database
# Create your views here.
def agrodata(request):
    return render(request, 'agrodata/agrodata.html', {})

def foodindustrydata(request):
    databases = Database.objects.all()
    context = {
        'databases': databases,  
    }
    return render(request, 'agrodata/foodindustrydata.html', context)