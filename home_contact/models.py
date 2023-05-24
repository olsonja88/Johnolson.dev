from django.db import models

class AboutParagraph(models.Model):
    title = models.CharField(max_length=25)
    photo = models.FilePathField(path="/home_contact/img")
    content = models.TextField()
