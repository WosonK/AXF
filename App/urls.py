from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^market/$', views.market, name='market'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^my/$', views.my, name='my'),
    url(r'^order$', views.order, name='order'),
]