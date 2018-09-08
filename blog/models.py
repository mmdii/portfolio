from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_data = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


    # ways to make new models
    # 1 - create A Blog models
    # 2 - add the blog app to the setting
    # 3 - create a migration
    # 4 - migrate
    # 5 - add to the admin