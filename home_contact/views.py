from django.shortcuts import render
from home_contact.models import AboutParagraph

def home(request):
    aps = AboutParagraph.objects.all()
    context = {
        'aps': aps
    }
    return render(request, 'home.html', context)
