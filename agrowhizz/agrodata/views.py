from django.shortcuts import render, get_object_or_404
from .models import Database, Company, CompanyAddress
from django.contrib.auth.decorators import login_required
# Create your views here.
def agrodata(request):
    
    return render(request, 'agrodata/agrodata.html', {})

@login_required
# view for all the food classification #
def foodindustrydata(request):
    databases = Database.objects.all().order_by('name')
    context = {
        'databases': databases,  
    }
    return render(request, 'agrodata/foodindustrydata.html', context)

# View for all the Comany Name #
def companyList(request, pk):
    databases = Database.objects.get(pk=pk)
    companies = databases.companies.order_by('company_name')
    
    context = {
        'databases': databases,
        'companies': companies,
        
    }
    return render(request, 'agrodata/companyList.html', context)

def companyDetails(request, pk, company_pk):
    
    company = get_object_or_404(Company, database__pk=pk, pk=company_pk)
    addresses = company.companyAddress.get()
    context = {
       
       'company': company,
       'addresses': addresses,
       
        
    }
    return render(request, 'agrodata/companyDetails.html', context)