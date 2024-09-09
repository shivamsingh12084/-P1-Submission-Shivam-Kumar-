from django.db import models

class FoodFacilityPermit(models.Model):
    locationid = models.CharField(max_length=100, primary_key=True)  
    applicant = models.CharField(max_length=500)  
    facility_type = models.CharField(max_length=200)  
    cnn = models.CharField(max_length=100, null=True, blank=True)  
    location_description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=500)  
    blocklot = models.CharField(max_length=200, null=True, blank=True)  
    block = models.CharField(max_length=200, null=True, blank=True)  
    lot = models.CharField(max_length=200, null=True, blank=True)  
    permit = models.CharField(max_length=200)  
    status = models.CharField(max_length=100)  
    food_items = models.TextField(null=True, blank=True)  
    x = models.CharField(max_length=50, null=True, blank=True)  # Changed from DecimalField
    y = models.CharField(max_length=50, null=True, blank=True)  # Changed from DecimalField
    latitude = models.CharField(max_length=50, null=True, blank=True)  # Changed from DecimalField
    longitude = models.CharField(max_length=50, null=True, blank=True)  # Changed from DecimalField
    schedule = models.URLField(null=True, blank=True)
    dayshours = models.CharField(max_length=500, null=True, blank=True)  
    noi_sent = models.CharField(max_length=200, null=True, blank=True)  
    approved = models.DateTimeField(null=True, blank=True)
    received = models.CharField(max_length=100, null=True, blank=True)  
    prior_permit = models.BooleanField(default=False)
    expiration_date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)  
    fire_prevention_districts = models.CharField(max_length=50, null=True, blank=True)  # Changed from IntegerField
    police_districts = models.CharField(max_length=50, null=True, blank=True)  # Changed from IntegerField
    supervisor_districts = models.CharField(max_length=50, null=True, blank=True)  # Changed from IntegerField
    zip_codes = models.CharField(max_length=50, null=True, blank=True)  # Changed from IntegerField
    neighborhoods_old = models.CharField(max_length=200, null=True, blank=True) 

    def __str__(self):
        return f"{self.applicant} - {self.locationid}"
