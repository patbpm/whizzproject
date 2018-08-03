from django.shortcuts import render

# Create your views here.
def agrodata(request):
    return render(request, 'agrodata/agrodata.html', {})

def foodindustrydata(request):
    return render(request, 'agrodata/foodindustrydata.html', {})