# Generated by Django 5.0.4 on 2024-05-18 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_photoevenement_is_first_photohistoire_is_first_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RessourceNaturelle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.commune')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoRessourceNaturelle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_first', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='photos/RessourceNaturelle')),
                ('ressource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.ressourcenaturelle')),
            ],
        ),
        migrations.CreateModel(
            name='CommentaireRessource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.utilisateur')),
                ('ressource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.ressourcenaturelle')),
            ],
        ),
    ]
