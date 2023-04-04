from django.contrib import admin
from .models import *

@admin.register(For_me)
class For_meAdmin(admin.ModelAdmin):
    list_display = ['name', 'avail']

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ['name', 'avail']
class ImagesInline(admin.StackedInline):
    model = Images
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Keys)
class KeysAdmin(admin.ModelAdmin):
    list_display = ['name','available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImagesInline,]

@admin.register(Zaiavki)
class ZaiavkiAdmin(admin.ModelAdmin):
    list_display = ['name','svaz','status','available']
    list_filte = ['date']

@admin.register(Nevs)
class NevsAdmin(admin.ModelAdmin):
    list_display = ['name','available']
    list_filte = ['date']



