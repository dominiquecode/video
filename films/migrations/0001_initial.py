# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acteur',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date_naissance', models.DateField(blank=True, default='1900-01-01')),
                ('date_deces', models.DateField(blank=True, default='1900-01-01')),
                ('nom', models.CharField(max_length=50, unique=True)),
                ('prenom', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('annee', models.IntegerField()),
                ('status', models.CharField(max_length=10, choices=[(None, 'Choisissez'), ('ACHETE', 'Acheté'), ('LOUE', 'Loué'), ('PRETE', 'Prêté')])),
                ('resume', models.TextField()),
                ('appreciation', models.CharField(max_length=10, choices=[(None, 'Choisissez'), ('EXCELLENT', 'Excellent'), ('TRESBON', 'Trés bon'), ('BON', 'Bon'), ('MOYEN', 'Moyen'), ('MEDIACRE', 'Médiacre'), ('NAVET', 'Navet')])),
                ('photo', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nom_pays', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Realisateur',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date_naissance', models.DateField(blank=True, default='1900-01-01')),
                ('date_deces', models.DateField(blank=True, default='1900-01-01')),
                ('nom', models.CharField(max_length=50, unique=True)),
                ('prenom', models.CharField(max_length=20, unique=True)),
                ('nom_pays', models.ForeignKey(to='films.Pays', to_field='nom_pays')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Type_film',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('type', models.CharField(max_length=20, unique=True)),
                ('commentaire', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='nom_pays',
            field=models.ForeignKey(to='films.Pays', to_field='nom_pays'),
        ),
        migrations.AddField(
            model_name='film',
            name='realisateur',
            field=models.ForeignKey(to='films.Realisateur', to_field='nom'),
        ),
        migrations.AddField(
            model_name='film',
            name='type_film',
            field=models.ForeignKey(to='films.Type_film', to_field='type'),
        ),
        migrations.AddField(
            model_name='acteur',
            name='nom_pays',
            field=models.ForeignKey(to='films.Pays', to_field='nom_pays'),
        ),
    ]
