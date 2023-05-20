from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from home_contact.models import AboutParagraph
from .forms import ContactForm

def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            body = form.cleaned_data["body"]
            try:
                send_mail(name, body, email, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid Header Found.")
            return redirect("success")
        
    aps = AboutParagraph.objects.all()
    context = {
        'aps': aps,
        'form': form
    }

    return render(request, 'home.html', context)

def success(request):
    return render(request, 'success.html')
