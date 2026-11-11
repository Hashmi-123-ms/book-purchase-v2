from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('add_form/', views.add_form, name='add_form'),
    path("signup/",views.register, name="signup"),
    path("login/",views.user_login,name="signin"),
    path('order-success/', views.order_success, name='order_success'),
    path('order/', views.order, name='order'),

]
