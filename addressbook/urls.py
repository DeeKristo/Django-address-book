from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('create_contact', views.createAddress, name='createAddress'),
    path('update_contact/<int:id>/', views.updateAddress, name='updateAddress'),
    path('delete/<int:id>/', views.deleteAddress, name='deleteAddress'),
    #path('<int:id>/', views.updateAddress, name='updateAddress'),
    path('addresssearch', views.searchAddress, name='searchAddress'),
]