from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import F, FloatField, Func, ExpressionWrapper
from django.db.models.functions import Cast
from .models import FoodFacilityPermit
from .serializers import FoodFacilityPermitSerializer
import math

# Haversine formula implementation
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Difference in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    # Haversine formula
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Distance in kilometers
    distance = R * c
    return distance

class FoodTruckView(APIView):
    def get(self, request):
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')

        if not latitude or not longitude:
            return Response({"error": "Latitude and longitude are required"}, status=400)

        # Convert latitude and longitude to float
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            return Response({"error": "Invalid latitude or longitude"}, status=400)

        # Calculate distances using Haversine formula
        food_trucks = FoodFacilityPermit.objects.all()
        distances = []
        for truck in food_trucks:
            truck_lat = float(truck.latitude) if truck.latitude else 0
            truck_lon = float(truck.longitude) if truck.longitude else 0
            distance = haversine(latitude, longitude, truck_lat, truck_lon)
            distances.append((truck, distance))
        
        # Sort by distance and get the 5 closest food trucks
        distances.sort(key=lambda x: x[1])
        nearest_trucks = [truck for truck, _ in distances[:5]]
        
        serializer = FoodFacilityPermitSerializer(nearest_trucks, many=True)
        return Response(serializer.data)
