from django.shortcuts import render
from .models import Business_stream
# Create your views here.
def agrodata(request):
    return render(request, 'agrodata/agrodata.html', {})

def foodindustrydata(request):
    business_streams = Business_stream.objects.all()
    context = {
        'business_streams': business_streams,  
    }
    return render(request, 'agrodata/foodindustrydata.html', context)