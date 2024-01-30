from django.db import models

class ShortUrls(models.Model):
    short_url = models.CharField(max_length=20)
    long_url = models.URLField("URL")

    def __str__(self):
        return f"Short URL: {self.short_url}, Long URL: {self.long_url}"
