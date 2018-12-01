from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=False,
                              upload_to='photos',
                              verbose_name="photo")
