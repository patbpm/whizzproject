from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.boards, name='boards'),
    url(r'^(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
]