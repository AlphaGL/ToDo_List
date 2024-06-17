from . import views

from django.urls import path
from .views import Home,About,Blog,News,Recipe
# from .views import contact, success


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('blog/', Blog.as_view(), name='blog'),
    # path('contact/', contact, name='contact'),
    # path('success/', success, name='success'),
    path('news/', News.as_view(), name='news'),
    path('recipe/', Recipe.as_view(), name='recipe'),

]