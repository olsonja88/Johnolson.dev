from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        }),
        required=True
    )
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "johnsmith123@gmail.com"
        }),
        required=True
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Message"
        }),
        required=True
    )
