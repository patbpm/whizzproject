
ffrom django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homePage, name='homePage'),
]