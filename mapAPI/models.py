from django.db import models

# Create your models here.

class LocationToAxis(models.Model):
    name=models.CharField(max_length=15)
    location=models.CharField(max_length=50, default='')
    
    # 위도, 경도
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)