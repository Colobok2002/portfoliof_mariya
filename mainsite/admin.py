from django.contrib import admin
from .models import *

@admin.register(For_me)
class For_meAdmin(admin.ModelAdmin):
    list_display = ['name', 'avail']

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ['name', 'avail']

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name']


class ImageskeysInline(admin.StackedInline):
    model = Images_keys

class ImagesnevsInline(admin.StackedInline):
    model = Images_nevs


@admin.register(Keys)
class KeysAdmin(admin.ModelAdmin):
    list_display = ['name','available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageskeysInline,]

@admin.register(Zaiavki)
class ZaiavkiAdmin(admin.ModelAdmin):
    list_display = ['name','svaz','status','date','available']
    list_filter  = ['date','available']

@admin.register(Nevs)
class NevsAdmin(admin.ModelAdmin):
    list_display = ['name','available']
    list_filter  = ['date','available']
    inlines = [ImagesnevsInline, ]


@admin.register(Contakts)
class ContaktsAdmin(admin.ModelAdmin):
    None




