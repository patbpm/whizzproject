from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homePage, name='homePage'),
    url(r'^whatWeDo/$', views.whatWeDo, name='whatWeDo'),
    url(r'^whatWeServe/$', views.whatWeServe, name='whatWeServe'),
]