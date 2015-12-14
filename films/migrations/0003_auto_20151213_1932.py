# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20151213_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acteur',
            name='nom',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='acteur',
            name='nom_pays',
            field=models.ForeignKey(to='films.Pays'),
        ),
        migrations.AlterField(
            model_name='acteur',
            name='prenom',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='film',
            name='nom_pays',
            field=models.ForeignKey(to='films.Pays'),
        ),
        migrations.AlterField(
            model_name='film',
            name='realisateur',
            field=models.ForeignKey(to='films.Realisateur'),
        ),
        migrations.AlterField(
            model_name='film',
            name='type_film',
            field=models.ForeignKey(to='films.Type_film'),
        ),
        migrations.AlterField(
            model_name='realisateur',
            name='nom',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='realisateur',
            name='nom_pays',
            field=models.ForeignKey(to='films.Pays'),
        ),
        migrations.AlterField(
            model_name='realisateur',
            name='prenom',
            field=models.CharField(max_length=20),
        ),
    ]
