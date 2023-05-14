from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError

#model Service
class Service(models.Model): # création du model Service 
    nom = models.CharField(max_length=50, primary_key=True) #nom du service , clé primaire
    description = models.CharField(max_length=500, default='') # text descriptif du services limite à 500 chr et par défault la valeur est ''
    prix = models.FloatField(default=0,validators=[MinValueValidator(0), MaxValueValidator(9999)]) # champs prix qui est un entier avec une valeur mini=0 et max =9999
    image = models.ImageField(upload_to='image_service',
                                default='image_service/default.png',) # image du service par défault une image est chargé (à choisir)
    def image_url(self):
        return self.image.url # récupere le lien de l'image sur notre projet pour pouvoir l'affiché plus facilement (pas sur de la pertinence)
    def __str__(self):
        return self.nom
    class Meta:
        verbose_name='Service'
        verbose_name_plural='Services'
#model Formulaire associé à services par nom de services

class Devis(models.Model): # créer class Formulaire
    Last_name = models.fields.CharField(max_length=50, default='', help_text='Nom de famille') #objet nom avec charactère 50, défault vide et affiche un texte d'aide pour donné un indice sur ce qu'il faut mettre
    First_name= models.fields.CharField(max_length=50, default='', help_text='Prénom') #objet prénom avec charactère 50, défault vide et affiche un texte d'aide pour donné un indice sur ce qu'il faut mettre
    adresse = models.CharField(max_length=200, help_text='1 rue des abricotiers')  #lieu de préstation charactère max 200
    ville = models.CharField(max_length=50, help_text='Paris') # idem pour le champs ville
    code_postal = models.CharField( 
        max_length=5,
        verbose_name='Code postal',
        help_text='Entrez un code postal valide',
        validators=[
            RegexValidator( # fonction qui permet de vérifier selon le critère regex
            regex=r'^[0-9]{5}$', #vérifie que le code postal est bien un ensemble de 5 chiffre de 0 à 9
            message='Le code postal doit contenir 5 chiffres', # affichie un message d'aide
            )
        ]
    ) 
    pays = models.CharField(max_length=50, help_text='France') #idem que pour l'adresse
    tel = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', 'Le numéro de téléphone doit comporter 10 chiffres.')], default='', help_text='Numéro de téléphone')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=None)

    def clean_pays(self): # fonction qui va venir vérifier que le pays sélectionné est bien la france mais je pense la supprimé
        if self.pays.lower() != 'france':
            raise ValidationError("Le pays doit être 'France'")
        return self.pays
    class Meta:
        verbose_name='Devis'
        verbose_name_plural='Devis'