# Generated by Django 2.2 on 2023-11-03 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20231103_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departement',
            name='domaine',
        ),
    ]
