from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    tittle = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    question = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.tittle

    def get_image(self):
        if self.image:
            return self.image.url

    class Meta():
        verbose_name_plural = 'Blog'

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    contact = models.TextField()

    class Meta():
        verbose_name_plural = 'Message'

    def __str__(self):
        return self.name
