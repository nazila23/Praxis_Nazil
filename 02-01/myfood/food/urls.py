from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('index/', views.index, name='index'), 
    path('<id>/delete/', views.deleteindex),
    path('<id>/detail/', views.detailindex),
    path('<id>/update/', views.updateindex),
    path('minuman/', views.minuman, name='minuman'), 
    path('minuman/<id>/delete/', views.deleteminum),
    path('minuman/<id>/detail/', views.detailminum),
    path('minuman/<id>/update/', views.updateminum),
    path('pesanan/', views.pesanan, name='pesanan'), 
    path('pesanan<id>/delete/', views.deletepesanan),
    path('pesanan<id>/detail/', views.detailpesanan),
    path('pesanan<id>/update/', views.updatepesanan),


]