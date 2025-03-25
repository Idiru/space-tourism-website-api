from django.db import models

class Crew(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(default="http://example.com")

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    avg_distance = models.IntegerField()
    est_travel_time = models.IntegerField()
    url = models.URLField(default="http://example.com")
    
    def __str__(self):
        return self.name
    
class Technologie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(default="http://example.com")


    def __str__(self):
        return self.name

