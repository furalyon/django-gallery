from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from . import models

class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = '__all__'

    def clean(self):
        if models.Photo.objects.all().count() >= settings.MAX_PHOTO_COUNT:
            raise forms.ValidationError(
                _('You can have a maximum of {0} photo(s) across'
                    ' all albums. Delete some old photos to add new'.format(
                    settings.MAX_PHOTO_COUNT)))
        return self.cleaned_data

class PhotoAdmin(admin.ModelAdmin):
    form = PhotoForm

admin.site.register(models.Album, AlbumAdmin)
admin.site.register(models.Photo, PhotoAdmin)