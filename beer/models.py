from django.db import models

BEER_CHOICES = (
    (1, 'Domestic'),
    (2, 'Import'),
)


class Beer(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    brewery = models.ForeignKey('Brewery')
    foto = models.CharField(max_length=60, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()
    locality = models.IntegerField(choices=BEER_CHOICES)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'beer'
        
    def __unicode__(self):
        return self.name
        

class Brewery(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name