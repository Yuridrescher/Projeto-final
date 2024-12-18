# Generated by Django 5.1.2 on 2024-11-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0004_alter_cardapio_semana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapio',
            name='semana',
            field=models.IntegerField(choices=[(2, 'Segunda-Feira'), (3, 'Terça-Feira'), (4, 'Quarta-Feira'), (5, 'Quinta-Feira'), (6, 'Sexta-Feira')]),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
