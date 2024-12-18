from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.TextField(default="Default summary")
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True) 
    youtube_link = models.URLField(blank=True, null =True)
    song_title = models.CharField(max_length=200, null=True, blank=True)  # Song title and artist
    song_message = models.TextField(null=True, blank=True)  # Custom message for the song section




    def __str__(self):
        return self.title