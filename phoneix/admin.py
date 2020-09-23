from django.contrib import admin
from .models import Glasse,Watche,Contactinfo

# Register your models here.

class GlasseAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'rating', 'shipin_date')


class WatcheAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'rating', 'shipin_date')


class ContactinfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'cancel')


admin.site.register(Watche, WatcheAdmin)
admin.site.register(Glasse, GlasseAdmin)
admin.site.register(Contactinfo, ContactinfoAdmin)