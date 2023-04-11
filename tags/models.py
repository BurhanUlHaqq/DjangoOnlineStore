from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tags(models.Model):
    tag=models.CharField(max_length=255)
    
class TaggedItem(models.Model):
    tag=models.ForeignKey(Tags,on_delete=models.CASCADE)
    
    #generic Content
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey()

