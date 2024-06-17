from . import views

from django.urls import path
# from .views import Home,About,Blog,News,Recipe
# from .views import contact, success


urlpatterns = [
    path('', views.cart_summary, name='summary'),
    path('add/', views.cart_add, name='add'),
    path('delete/', views.cart_delete, name='delete'),
    path('update/', views.cart_update, name='update'),
]