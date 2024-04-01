from django import forms



class CakeForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    weight = forms.DecimalField()
    price = forms.DecimalField()
    image = forms.ImageField()
    stars = forms.FloatField()

class EmailForm(forms.Form):
    address = forms.CharField(max_length=100)
    title = forms.CharField(max_length=32)
    message = forms.CharField(widget=forms.Textarea)

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=32)

