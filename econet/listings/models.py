from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError

#model Service
class Service(models.Model):
    id = models.CharField(max_length=50, primary_key=True) #nom du service , clé primaire
    sequence = models.CharField(max_length=500, default='') # text descriptif du services
    prix = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(9999)])
    picture = models.ImageField(upload_to='profile_pic',
                                default='profile_pic/default.png')

#model Formulaire associé à services par nom de services

class Formulaire(models.Model):
    Last_name = models.fields.CharField(max_length=50, default='', help_text='Nom de famille')
    First_name= models.fields.CharField(max_length=50, default='', help_text='Prénom')
    adresse = models.CharField(max_length=200, help_text='1 rue des abricotiers')  #lieu de préstation
    ville = models.CharField(max_length=50)
    code_postal = models.CharField(
        max_length=5,
        verbose_name='Code postal',
        help_text='Entrez un code postal valide',
        validators=[
            RegexValidator(
            regex=r'^[0-9]{5}$',
            message='Le code postal doit contenir 5 chiffres',
            )
        ]
    )
    pays = models.CharField(max_length=50)

    
    def clean_pays(self):
        if self.pays.lower() != 'france':
            raise ValidationError("Le pays doit être 'France'")
        return self.pays