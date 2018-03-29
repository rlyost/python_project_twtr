from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='in'),
    url(r'^grab$', views.grab, name='grab'),
]