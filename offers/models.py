from django.db import models


class BannerImages(models.Model):
    image_field = models.FileField(upload_to='images/banners')

    def __str__(self):
        return self.image_field.name



