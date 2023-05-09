from django.db import models

class Sprite(models.Model):
    name = models.CharField(max_length=20)
    image = models.FilePathField(path="/gameassets/img")

class Animation(models.Model):
    name = models.CharField(max_length=20)
    gif = models.FilePathField(path="/gameassets/gif")

class Soundtrack(models.Model):
    name = models.CharField(max_length=20)
    mp3 = models.FilePathField(path="/gameassets/mp3")
