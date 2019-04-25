from django.conf.urls import url
from . import views
from django.urls import path
app_name='cookieapp'
urlpatterns=[
    url(r'^$', views.input),
    url(r'^add$', views.add),
    url(r'^display$', views.display),
]