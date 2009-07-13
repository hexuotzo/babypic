from django.db import models    
from django.contrib.sites.models import Site
class FlatPage(models.Model):  
    title = models.CharField(maxlength=200)  
    content = models.TextField()  
    sites = models.ManyToManyField(Site)