from datetime import timezone

from django.db import models
from ckeditor.fields import RichTextField

class Madini(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    images = models.FileField(upload_to='images/madini')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    def __str__(self):

        return self.title

    class Meta:
        ordering = ['-created_at']