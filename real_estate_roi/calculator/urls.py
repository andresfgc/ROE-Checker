# calculator/urls.py
from django.urls import path
from .views import home, calculate_buy_fix_sell, calculate_buy_fix_rent

urlpatterns = [
    path('', home, name='home'),
    path('calculate-buy-fix-sell/', calculate_buy_fix_sell, name='calculate_buy_fix_sell'),
    path('calculate-buy-fix-rent/', calculate_buy_fix_rent, name='calculate_buy_fix_rent'),
]
