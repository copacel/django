from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Article(models.Model):
    title   = models.CharField(max_length=255,blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)