from django.db import models

class AboutParagraph(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
