from django.db import models

BEER_CHOICES = (
    (1, 'Domestic'),
    (2, 'Import'),
)

class Beer(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    brewery = models.ForeignKey('Brewery')
    locality = models.IntegerField(choices=BEER_CHOICES)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
        

class Brewery(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name