from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.agrodata, name='agrodata'),
    url(r'^foodindustrydata/$', views.CompanyCategoryListView.as_view(), name='foodindustrydata'),
    url(r'^foodcategoriesdata/$', views.FoodCategoryListView.as_view(), name='foodcategoriesdata'),
    url(r'^foodindustrydata/(?P<pk>\d+)/$', views.companyList, name='companyList'),
    url(r'^foodcategoriesdata/(?P<pk>\d+)/$', views.ingredientList, name='ingredientList'),
    url(r'^foodindustrydata/(?P<pk>\d+)/companydetails/(?P<company_pk>\d+)/$', views.companyDetails, name='companyDetails'),
    url(r'^foodcategoriesdata/(?P<pk>\d+)/ingredientdetails/(?P<ingredient_pk>\d+)/$', views.ingredientDetails, name='ingredientDetails'),
]