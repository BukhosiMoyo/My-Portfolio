from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, label="", widget = forms.TextInput(attrs ={'placeholder':'Your name'}))
    email = forms.EmailField(required=True, label="", widget = forms.TextInput(attrs ={'placeholder':'Your email'}))
    subject = forms.CharField(required=True, label="", widget = forms.TextInput(attrs ={'placeholder':'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs ={'placeholder':'Your message'}), required=True, label="")
