from django.db import models


class Videos(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.CharField(max_length=1000)
    images = models.FileField(upload_to='images/videos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']