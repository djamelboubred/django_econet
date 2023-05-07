from django.contrib import admin
from listings.models import Service, Devis
from django.utils.translation import gettext_lazy as lazy

#class CustomAdminSite(admin.AdminSite):
#    class Media:
#        css = {
#            'all': ('css/custom_admin.css',),
#        }
#admin.site.register(CustomAdminSite)

@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display=('nom','description','prix','image')
    class Meta:
        verbose_name='Service'
        verbone_name_plural='Services'

@admin.register(Devis)
class Devis(admin.ModelAdmin):
    list_display=('Last_name','First_name','code_postal',)

admin.site.site_title= lazy("Econet Admin") #modifie le titre enn Econet System (j'ai pas vu ou il est modifé mais je le met au cas ou)
admin.site.site_header = lazy("Econet Admin") #modifie l'header enn Econet System
admin.site.index_title = lazy("Econet Admin") #modifie l'index enn Econet System