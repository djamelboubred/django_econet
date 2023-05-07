from django.shortcuts import render
from .forms import ServiceForm
from listings.models import Service

def home(request): # creer une requête pour la page home qui va venir prendre la page home.html est juste affiché le code html
    service = Service.objects.all()
    return render(request, 'listings/home.html')

def service(request): # creer une requête pour la page service qui va venir prendre la page service.html est juste affiché le code html
    return render(request, "listings/Services.html")

#def add_service(request): # creer une requête pour la page add_service
#    if request.method == 'POST': #vérifie que la méthode est bien en POST si oui on lance le formulaire
#        form = ServiceForm(request.POST, request.FILES) #créer le formulaire
#        if form.is_valid(): 
#            service = form.save(commit=False)
#            service.id = form.cleaned_data['id'] #form pour le champs id de la classe service creer dans model.py
#            service.description = form.cleaned_data['description'] #form pour le champs description de la classe service dans le model.py
#            service.prix = form.cleaned_data['prix'] #idem pour le champ prix
#            service.picture = form.cleaned_data['picture'] #idem pour le champs picture
#            service.save()
#            return redirect('confirmation')
#    else:
#        form = ServiceForm()
#    return render(request, 'listings/add_service.html', {'form': form}) #retourne dans le fichier add.services pour afficher son contenue

