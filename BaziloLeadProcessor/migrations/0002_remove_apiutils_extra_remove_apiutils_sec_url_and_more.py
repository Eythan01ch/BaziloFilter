# Generated by Django 4.0.4 on 2022-05-31 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BaziloLeadProcessor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apiutils',
            name='extra',
        ),
        migrations.RemoveField(
            model_name='apiutils',
            name='sec_url',
        ),
        migrations.RemoveField(
            model_name='apiutils',
            name='url',
        ),
    ]
