# Generated by Django 3.0.5 on 2020-04-06 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
