from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Drinker(models.Model):
    user = models.OneToOneField(User, unique=False)
    name = models.CharField(max_length=140)
    birthday = models.DateField(null=True)
    
    def __unicode__(self):
        return self.name
    

# create our user object to attach drinker
#def create_drinker_user_callback(sender, instance, **kwargs):
    #drinker, new = Drinker.objects.get_or_create(user=instance)
    
#post_save.connect(create_drinker_user_callback, User)