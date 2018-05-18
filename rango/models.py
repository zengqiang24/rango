from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
class Category(models.Model):
    name=models.CharField(max_length=128,unique=type)
    views=models.IntegerField(default=0)
    likes=models.IntegerField(default=0)
    slug=models.SlugField()

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user=models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username