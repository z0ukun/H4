# coding=utf-8
from django.contrib import admin
from models import *


class HeroInfoInline(admin.StackedInline):
    model = heroinfo
    extra = 3


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub']
    list_filter = ['btitle']
    search_fields = ['id', 'btitle', 'bpub']
    list_per_page = 2
    fieldsets = [
        ('base', {'fields': ['btitle']}),
        ('super', {'fields': ['bpub']}),
    ]
    inlines = HeroInfoInline,


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender', 'hcontent', 'hbook']
    list_filter = ['id', 'hname']


# Register your models here.
admin.site.register(bookinfo, BookInfoAdmin)
admin.site.register(heroinfo, HeroInfoAdmin)
