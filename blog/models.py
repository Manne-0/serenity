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


class Moment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, blank=True, null=True)  # Optional

    def __str__(self):
        return self.title



class MomentMedia(models.Model):
    moment = models.ForeignKey(Moment, related_name='media', on_delete=models.CASCADE)
    file = models.FileField(upload_to='moments_media/')
    is_video = models.BooleanField(default=False)  # Flag to differentiate videos from images

    def __str__(self):
        return f"Media for {self.moment.title}"