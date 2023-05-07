from django import forms
from .models import Service

class ServiceForm(forms.ModelForm): #creer la structure du formulaire pour la classe Service
    class Meta:
        model = Service
        fields = ['nom', 'description', 'prix', 'image'] # prend l'ensemble des champs pour la structrure du formulaire