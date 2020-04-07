
from django.db import models
# Create your models here.
from django.db.models.fields.files import ImageFieldFile
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
        title = models.CharField(max_length=150)
        keyword = models.CharField(max_length=30)
        description = models.CharField(max_length=30)
        image=models.ImageField(blank=True, null=True,upload_to='images/')
        parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
        create_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)
        slug=models.SlugField(null=True)
        STATUS = (
            ('True', 'Evet'),
            ('False', 'Hayır'),
        )
        status = models.CharField(max_length=30, choices=STATUS)
        def __str__(self):
                return self.title

class Product(models.Model):
        title = models.CharField(max_length=150)
        keyword = models.CharField(max_length=30)
        description = models.CharField(max_length=30)
        image = models.ImageField(blank=True, null=True, upload_to='images/')
        category = models.ForeignKey('Category', on_delete=models.CASCADE)
        create_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)
        slug = models.SlugField(null=True)
        detail = RichTextUploadingField()
        STATUS = (
                ('True', 'Evet'),
                ('False', 'Hayır'),
        )
        status = models.CharField(max_length=30, choices=STATUS)

        def __str__(self):
                return self.title

        def image_tag(self):
                return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
                image_tag.short_description = 'Image'

class Images(models.Model):
        produt=models.ForeignKey(Product,on_delete=models.CASCADE)
        title=models.CharField(max_length=50)
        image=models.ImageField(blank=True, null=True,upload_to='images/')

        def __str__(self):
                return self.title

