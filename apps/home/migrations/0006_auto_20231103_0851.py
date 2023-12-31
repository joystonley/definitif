# Generated by Django 2.2 on 2023-11-03 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20231030_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='departement',
            name='domaine',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='departements', to='home.Domaine'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employe',
            name='prenom_em',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='indice',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='prenom_en',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
