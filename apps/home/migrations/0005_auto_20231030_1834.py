# Generated by Django 2.2 on 2023-10-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20231030_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corps',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
