from .models import Registration
from django.forms import ModelForm, TextInput


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = ["name", "surname", "login", "password"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'place-holder': 'Введите имя'}),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'place-holder': 'Введите фамилию'}),
            "login": TextInput(attrs={
                'class': 'form-control',
                'place-holder': 'Введите название'}),
            "password": TextInput(attrs={
                'class': 'form-control',
                'place-holder': 'Введите название'}),
        }
