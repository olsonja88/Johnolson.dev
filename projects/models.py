from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    gh_url = models.URLField(null=True)
    image = models.FilePathField(path="/projects/img")
