from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'), 
    path('', views.home, name='home'), 
    path('minuman/', views.minuman, name='minuman'), 
    path('pesanan/', views.pesanan, name='pesanan'), 
    path('<id>/delete/', views.deleteindex),
    path('<id>/detail/', views.detailindex),
    path('<id>/update/', views.updateindex),
    path('<id>/delete/', views.deleteminum),
    path('<id>/detail/', views.detailminum),
    path('<id>/update/', views.updateminum),
    path('<id>/delete/', views.deletepesan),
    path('<id>/detail/', views.detailpesan),
    path('<id>/update/', views.updatepesan),


]