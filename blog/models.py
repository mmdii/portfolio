from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_data = models.DateTimeField()
    body = models.TextField()
    image = image = models.ImageField(upload_to='images/')