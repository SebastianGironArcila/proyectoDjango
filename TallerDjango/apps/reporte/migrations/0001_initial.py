# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 04:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadEntregasAnuales', models.IntegerField()),
                ('año', models.IntegerField()),
                ('registrante', models.CharField(max_length=50)),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedor.Proveedor')),
            ],
        ),
    ]
