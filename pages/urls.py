from django.urls import path
from .views import FoodTruckView

urlpatterns = [
    path('food-trucks/', FoodTruckView.as_view(), name='food_truck_list'),
]