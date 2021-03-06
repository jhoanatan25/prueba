# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-15 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_remove_car_zip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='vin',
        ),
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.CharField(choices=[('Nuevo', 'nuevo'), ('Usado', 'usado'), ('Certificado', 'Certificado')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(blank=True, choices=[(2, 'Dos'), (3, 'Tres'), (4, 'Cuatro'), (5, 'Cinco')], null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='exterior_color',
            field=models.CharField(blank=True, choices=[('Negro', 'Negro'), ('Azul', 'Azul'), ('Marrón', 'Marrón'), ('Dorado', 'Dorado'), ('Gris', 'Gris'), ('Verde', 'Verde'), ('Blanco oscuro', 'Blanco oscuro'), ('Rojo', 'Rojo'), ('Plateado', 'Plateado'), ('Blanco', 'Blanco'), ('Violeta', 'Violeta'), ('Naranja', 'Naranja'), ('Otro', 'Otro')], max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='interior_color',
            field=models.CharField(blank=True, choices=[('Negro', 'Negro'), ('Azul', 'Azul'), ('Marrón', 'Marrón'), ('Dorado', 'Dorado'), ('Gris', 'Gris'), ('Verde', 'Verde'), ('Blanco oscuro', 'Blanco oscuro'), ('Rojo', 'Rojo'), ('Plateado', 'Plateado'), ('Blanco', 'Blanco'), ('Violeta', 'Violeta'), ('Naranja', 'Naranja'), ('Otro', 'Otro')], max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='interior_fabric',
            field=models.CharField(blank=True, choices=[('Tela', 'Tela'), ('Cuero', 'Cuero'), ('No aplica', 'No aplica'), ('Otro', 'Otro')], max_length=100),
        ),
    ]
