from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.agrodata, name='agrodata'),
    url(r'^foodindustrydata/$', views.foodindustrydata, name='foodindustrydata'),
]