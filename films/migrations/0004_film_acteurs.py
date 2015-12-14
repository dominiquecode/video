# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_auto_20151213_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='acteurs',
            field=models.ManyToManyField(to='films.Acteur'),
        ),
    ]
