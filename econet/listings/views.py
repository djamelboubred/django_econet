#from django.shortcuts import render, redirect
#from .forms import DevisForm 
#from listings.models import Service, Devis
# ##from django.core.mail import send_mail
##from django.core.mail import EmailMessage
#import os
#from django.conf import settings
#from django.core.mail import send_mail, BadHeaderError
#from django.http import HttpResponse
#from sendinblue import SibApiV3Sdk


import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import DevisForm
from listings.models import Service

def home(request): # creer une requête pour la page home qui va venir prendre la page home.html est juste affiché le code html
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'listings/home.html', context)

#def send_email(subject, message, from_email, to_email):
#    email = EmailMessage(
#        subject=subject,
#        body=message,
#        from_email=from_email,
#        to=[to_email],
#        reply_to=[from_email],
#    )
#    email.send()

def devis(request):
    services = Service.objects.all()
    if request.method == 'POST':
        form = DevisForm(request.POST)
        if form.is_valid():
            form.save()
            # Récupérer les informations de l'utilisateur et du formulaire
            nom = form.cleaned_data.get('Last_name')
            prenom = form.cleaned_data.get('First_name')
            #adresse = form.cleaned_data.get('adresse')
            #tel= form.cleaned_data.get('tel')
            #ville = form.cleaned_data.get('ville')
            #code_postal = form.cleaned_data.get('code_postal')
            #pays = form.cleaned_data.get('pays')
            service = form.cleaned_data.get('service')
            #message = f"Bonjour,\n\nVous avez reçu une demande de devis de {nom} {prenom} pour le service {service}. Voici les informations de contact de l'utilisateur :\n\nNom : {nom}\nPrénom : {prenom}\nAdresse : {adresse}\nVille : {ville}\nCode postal : {code_postal}\nPays : {pays}\nTéléphone : {tel}\n\nCordialement,\nL'équipe de votre entreprise"

            # Envoyer l'email
            sib_api_v3_sdk.configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
            api_instance = sib_api_v3_sdk.TransactionalEmailsApi()
            send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
                to=[{"email": form.cleaned_data.get('email'), "name": nom}],
                template_id=settings.SENDINBLUE_TEMPLATE_ID,
                params={
                    "name": nom,
                    "prenom": prenom,
                    #"adresse": adresse,
                    #"tel": tel,
                    #"ville": ville,
                    #"code_postal": code_postal,
                    #"pays": pays,
                    "service": service
                }
            )
            try:
                api_response = api_instance.send_transac_email(send_smtp_email)
                print("API response status: %s" % api_response.status)
            except ApiException as e:
                print("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)

            return render(request, 'listings/confirmation.html')
    else:
        form = DevisForm()
    return render(request, 'listings/devis.html', {'form': form, 'services': services})


#def devis(request):
#    services = Service.objects.all()
#    if request.method == 'POST':
#        form = DevisForm(request.POST)
#        if form.is_valid():
#            form.save()
#            # Récupérer les informations de l'utilisateur et du formulaire
#            nom = form.cleaned_data.get('Last_name')
#            prenom = form.cleaned_data.get('First_name')
#            adresse = form.cleaned_data.get('adresse')
#            tel= form.cleaned_data.get('tel')
#            ville = form.cleaned_data.get('ville')
#            code_postal = form.cleaned_data.get('code_postal')
#            pays = form.cleaned_data.get('pays')
#            service = form.cleaned_data.get('service')
#            message = f"Bonjour,\n\nVous avez reçu une demande de devis de {nom} {prenom} pour le service {service}. Voici les informations de contact de l'utilisateur :\n\nNom : {nom}\nPrénom : {prenom}\nAdresse : {adresse}\nVille : {ville}\nCode postal : {code_postal}\nPays : {pays}\nTéléphone : {tel}\n\nCordialement,\nL'équipe de votre entreprise"
#
#            # Envoyer l'email
#            from_email = 'votre_adresse_email@gmail.com' # Modifier avec votre adresse email
#            to_email = 'adresse_email_destinataire@gmail.com' # Modifier avec l'adresse email du destinataire
#            password = 'votre_mot_de_passe_gmail' # Modifier avec votre mot de passe Gmail
#
#            send_email('Nouvelle demande de devis', message, from_email, to_email, password)
#            return render(request, 'devis_confirmation.html')
#    else:
#        form = DevisForm()
#    return render(request, 'listings/devis.html', {'form': form, 'services': services})
##            # Envoi de l'email
##            subject = 'Nouvelle soumission de formulaire'
##            message = 'Un nouveau formulaire a été soumis. Les données sont les suivantes :\n\n{}'.format(form.cleaned_data)
##            from_email = 'djef.91860@gmail.com'
##            recipient_list = ['djamel.91860@gmail.com']
##            send_mail(subject, message, from_email, recipient_list)
##
##            # Redirection vers une page de confirmation
##            return render(request, 'listings/confirmation.html')
##    else:
#        form = DevisForm()
#
#    context = {'form': form}
#    return render(request, 'listings/devis.html', context)


#def Devis(request):
#    return render(request, 'listings/devis.html')
#
#def devis(request):
#    if request.method == 'POST':
#        form = DevisForm(request.POST)
#        if form.is_valid():
#            form.save()
#            #send_mail(
#            #    'Nouveau devis',
#            #    'Un nouveau devis a été soumis.',
#            #    'djef.91860@gmail.com',
#            #    ['djamel.91860@gmail.com'],
#            #    fail_silently=False,
#            #)
#    else:
#        form = DevisForm()
#
#    context = {'form': form}
#    return render(request, 'listings/devis.html', context)
#
#def SendDevis(request):
#    if request.method == 'POST':
#        # Récupération des données du formulaire
#        form_data = request.POST
#
#        # Envoi de l'email
#        subject = 'Nouvelle soumission de formulaire'
#        message = 'Un nouveau formulaire a été soumis. Les données sont les suivantes :\n\n{}'.format(form_data)
#        from_email = 'mon-adresse-email@example.com'
#        recipient_list = ['adresse-email-de-destination@example.com']
#        send_mail(subject, message, from_email, recipient_list)
#
#        # Redirection vers une page de confirmation
#        return render(request, 'listings/confirmation.html')
#
#    else:
#        # Affichage du formulaire
#        return render(request, 'listings/devis.html', {})
#
#