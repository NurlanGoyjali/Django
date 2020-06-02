from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models
# Create your models here.
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    title = models.CharField(max_length=150)
    keyword = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, unique=True)
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    status = models.CharField(max_length=30, choices=STATUS)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class MPTTMeta:
    order_insertion_by = ['title']


def __str__(self):
    full = [self.title]
    k = self.parent
    while k is not None:
        full.append(k.title)
        k = k.parent
    return '--->>'.join(full[::-1])


class Product(models.Model):
    title = models.CharField(max_length=150)
    keyword = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    price = models.CharField(max_length=15)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, unique=True)
    detail = RichTextUploadingField()
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    status = models.CharField(max_length=30, choices=STATUS)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        image_tag.short_description = 'Image'


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        image_tag.short_description = 'Image'


class Comment(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=500, blank=True)

    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(max_length=20, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment']
