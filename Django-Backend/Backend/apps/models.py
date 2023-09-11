from django.db import models

class EnergyData(models.Model):
    end_year = models.CharField(max_length=4, blank=True , null=True)
    intensity = models.IntegerField(null=True)
    sector = models.CharField(max_length=255 , null=True)
    topic = models.CharField(max_length=255 , null=True)
    insight = models.CharField(max_length=255)
    url = models.URLField(null=True)
    region = models.CharField(max_length=255,null=True)
    start_year = models.CharField(max_length=4, blank=True,null=True)
    impact = models.CharField(max_length=255, blank=True,null=True)
    added = models.DateTimeField(auto_now_add=False , auto_now=False,null=True)
    published = models.DateTimeField(auto_now_add=False , auto_now=False ,null=True)
    country = models.CharField(max_length=255,null=True)
    relevance = models.IntegerField(null=True)
    pestle = models.CharField(max_length=255,null=True)
    source = models.CharField(max_length=255,null=True)
    title = models.CharField(max_length=255,null=True)
    likelihood = models.IntegerField(null=True)

    def __str__(self):
        return self.title
