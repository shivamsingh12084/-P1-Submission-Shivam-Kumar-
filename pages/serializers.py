from rest_framework import serializers
from .models import FoodFacilityPermit

class FoodFacilityPermitSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodFacilityPermit
        fields = '__all__'