from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'), 
    path('', views.home, name='home'), 
    path('minuman/', views.minuman, name='minuman'), 
    path('<id>/delete/', views.delete),
    path('<id>/detail/', views.detail),
    path('<id>/update/', views.update),

]