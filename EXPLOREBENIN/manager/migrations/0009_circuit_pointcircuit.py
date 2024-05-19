# Generated by Django 5.0.4 on 2024-05-18 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_evenement_commune'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PointCircuit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordre', models.IntegerField()),
                ('circuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.circuit')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.evenement')),
                ('hist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.histoire')),
                ('res', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.ressourcenaturelle')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.sitetouristique')),
            ],
        ),
    ]