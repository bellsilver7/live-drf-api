import uuid

from django.db import models

from config.constants import STREAM_STATUS_CHOICES


# Create your models here.
class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    thumbnail = models.ImageField(null=True, upload_to='programs/')
    stream_status = models.CharField(max_length=20, choices=STREAM_STATUS_CHOICES)
    stream_scheduled_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
