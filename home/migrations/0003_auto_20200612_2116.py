# Generated by Django 3.0.5 on 2020-06-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='order_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
    ]
