# Generated by Django 3.1.3 on 2021-01-29 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0033_auto_20210128_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='hackathon_image',
            field=models.TextField(blank=True, default='', help_text='Hackathon image.'),
        ),
    ]
