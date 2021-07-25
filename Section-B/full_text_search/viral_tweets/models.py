from django.db import models


# Create your models here.
class ViralTweet(models.Model):
	user_handle = models.CharField(max_length=50)
	tweet = models.TextField(max_length=1000)

