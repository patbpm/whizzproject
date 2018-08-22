from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.agrodata, name='agrodata'),
    url(r'^foodindustrydata/$', views.foodindustrydata, name='foodindustrydata'),
    url(r'^foodindustrydata/(?P<pk>\d+)/$', views.companyList, name='companyList'),
    
]