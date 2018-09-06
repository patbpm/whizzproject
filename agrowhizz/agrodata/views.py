from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from .models import Database, Company, CompanyAddress, IngredientsCategories, Ingredients
from django.contrib.auth.decorators import login_required
# Create your views here.
def agrodata(request):
    
    return render(request, 'agrodata/agrodata.html', {})


# view for all the Company classification #
@method_decorator(login_required, name='dispatch')
class CompanyCategoryListView(ListView):
    model = Database
    context_object_name = 'databases'
    template_name = 'agrodata/foodindustrydata.html'
    ordering = 'name'

# view for all the food classification #    
@method_decorator(login_required, name='dispatch')
class FoodCategoryListView(ListView):
    model = IngredientsCategories
    context_object_name = 'foodCategories'
    template_name = 'agrodata/foodcategoriesdata.html'
    

# View for all the Company Name #
def companyList(request, pk):
    databases = Database.objects.get(pk=pk)
    companies = databases.companies.order_by('company_name')
    
    context = {
        'databases': databases,
        'companies': companies,
        
    }
    return render(request, 'agrodata/companyList.html', context)

# View for all the Company Name #
def ingredientList(request, pk):
    categories = IngredientsCategories.objects.get(pk=pk)
    ingredients = categories.Ingredients.order_by('name')
    
    context = {
        'categories': categories,
        'ingredients': ingredients,
        
    }
    return render(request, 'agrodata/ingredientList.html', context)

def companyDetails(request, pk, company_pk):
    
    company = get_object_or_404(Company, database__pk=pk, pk=company_pk)
    addresses = get_object_or_404(company.companyAddress)
    ingredients = company.Ingredients.all()
    categories = ingredients.order_by('category__category').values_list('category__category', flat=True).distinct()
    logos = get_object_or_404(company.CompanyLogo)

    context = {
       
       'company': company,
       'addresses': addresses,
       'categories': categories,
       'ingredients': ingredients,
       'logos': logos,
    }
    return render(request, 'agrodata/companyDetails.html', context)

def ingredientDetails(request, pk, ingredient_pk):
    
    ingredient = get_object_or_404(Ingredients, category__pk=pk, pk=ingredient_pk)
    details = get_object_or_404(ingredient.IngredientDetail)
    organoleptics = get_object_or_404(ingredient.ProductPhysicalProperty)
    pictures = get_object_or_404(ingredient.ProductPicture)

    context = {
       
       'ingredient': ingredient,
       'details': details,
       'organoleptics': organoleptics,
       'pictures': pictures,
    }
    return render(request, 'agrodata/ingredientDetails.html', context)