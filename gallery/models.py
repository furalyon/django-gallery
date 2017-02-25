import os

from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.core.urlresolvers import reverse

from easy_thumbnails.files import get_thumbnailer

class Album(models.Model):
    name = models.CharField(_('Name'), max_length=255, primary_key=True)
    slug = models.SlugField(_('Slug'), max_length=255, unique = True)
    date = models.DateField(_('date'))
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date',)

    def save(self, *args, **kwargs):
        if not(self.name):
            raise ValidationError(_('%s name cannot be empty'%self._meta.model_name))
        super(Album, self).save(*args, **kwargs)

    def thumbnail(self):
        photos = self.photos.all()
        return photos[0] if photos else None

    def get_absolute_url(self):
        return reverse('gallery:detail',args=(self.slug,))


def photo_location(instance, filename):
    return 'album/{0}/{1}'.format(
        instance.album.slug,
        filename)

class Photo(models.Model):
    album = models.ForeignKey('gallery.Album',
        verbose_name=_('album'), related_name='photos')
    image = models.ImageField(_('Image'), upload_to=photo_location,
        help_text=_('maximum file size {}'.format(
            filesizeformat(settings.MAX_PHOTO_SIZE))))
    
    def __str__(self):
        return '{0} - {1}'.format(self.album, self.image)

    class Meta:
        ordering = ('pk',)

    def save(self, *args, **kwargs):
        new_photo = not self.id
        super(Photo, self).save(*args, **kwargs)
        if new_photo:
            #shrink image
            org_file = self.image
            self.image = get_thumbnailer(
                self.image)['photo'].url.replace('/media','')
            self.save()
            os.remove(os.path.join(settings.MEDIA_ROOT,org_file.name))

# These two auto-delete files from filesystem when they are unneeded:
@receiver(models.signals.post_delete, sender=Photo)
def auto_delete_photo_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `Photo` object is deleted.
    """
    if instance.image:
        filepath = settings.MEDIA_ROOT+instance.image.name
        if os.path.isfile(filepath):
            os.remove(filepath)
