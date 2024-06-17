from . import views

from django.urls import path
from .views import Home,Appetizer,Beverage,Breakfast,Desert,Dinner,Lunch,MainCourse,Salad,SoupAndStew


urlpatterns = [
    # path('', Home.as_view(), name='home'),
    path('', Appetizer.as_view(), name='appetizer'),
    path('beverage/', Beverage.as_view(), name='beverage'),
    path('breakfast/', Breakfast.as_view(), name='breakfast'),
    path('desert/', Desert.as_view(), name='desert'),
    path('dinner/', Dinner.as_view(), name='dinner'),
    path('lunch/', Lunch.as_view(), name='lunch'),
    path('maincourse/', MainCourse.as_view(), name='maincourse'),
    path('salad/', Salad.as_view(), name='salad'),
    path('soupandstew/', SoupAndStew.as_view(), name='soupandstew'),

]