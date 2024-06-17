from . import views

from django.urls import path
from .views import Cake,Cocoa,Jollof,Meatballs,Omelette,Pasta,Straw,Tsire,Yam


urlpatterns = [
    # path('', Home.as_view(), name='home'),
    path('', Cake.as_view(), name='cake'),
    path('cocoa/', Cocoa.as_view(), name='cocoa'),
    path('jollof/', Jollof.as_view(), name='jollof'),
    path('meatballs/', Meatballs.as_view(), name='meatballs'),
    path('omelette/', Omelette.as_view(), name='omelette'),
    path('pasta/', Pasta.as_view(), name='pasta'),
    path('straw/', Straw.as_view(), name='straw'),
    path('tsire/', Tsire.as_view(), name='tsire'),
    path('yam/', Yam.as_view(), name='yam'),

]