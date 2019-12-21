from django.db import models

class PhysicsSite(models.Model):

    article_title = models.CharField(max_length=60)
    article_link = models.CharField(max_length=50)
    article_img = models.CharField(max_length=255)
    article_summary = models.CharField(max_length=255)

    def __str__(self):
        return self.article_img
