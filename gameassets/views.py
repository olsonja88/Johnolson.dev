from django.shortcuts import render
from gameassets.models import Sprite, Animation, Soundtrack

def gameasset_index(request):
    sprites = Sprite.objects.all()
    animations = Animation.objects.all()
    soundtracks = Soundtrack.objects.all()

    context = {
        'sprites': sprites,
        'animations': animations,
        'soundtracks': soundtracks
    }
    return render(request, 'gameasset_index.html', context)
