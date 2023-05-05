from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    email = forms.CharField(
        max_length=60,
        wigdet=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "johnsmith@gmail.com"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Meesage"
        })
    )
