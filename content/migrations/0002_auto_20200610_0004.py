# Generated by Django 3.0.5 on 2020-06-09 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='type',
            field=models.CharField(choices=[('menu', 'menu'), ('haber', 'haber'), ('duyuru', 'duyuru'), ('etkinlik', 'etkinlik')], default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]
