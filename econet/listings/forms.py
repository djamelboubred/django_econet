from django import forms
from .models import Service, Devis

class ServiceForm(forms.ModelForm): #creer la structure du formulaire pour la classe Service
    class Meta:
        model = Service
        fields = ['nom', 'description', 'prix', 'image'] # prend l'ensemble des champs pour la structrure du formulaire

class DevisForm(forms.ModelForm):
    class Meta:
        model=Devis
        fields = '__all__'
        service = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        to_field_name='nom',
        label='Service'
        )
        #widgets = {
        #    'service': forms.Select(choices=[(service.pk, service.nom) for service in Service.objects.all()])
        #}
        #def __init__(self, *args, **kwargs):
        #    super().__init__(*args, **kwargs)
        #    self.fields['service'].queryset = Service.objects.all()
        #    self.fields['service'].label = 'Service'