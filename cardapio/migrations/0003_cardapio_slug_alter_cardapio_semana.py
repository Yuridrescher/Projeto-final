# Generated by Django 5.1.2 on 2024-11-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0002_cardapio_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardapio',
            name='slug',
            field=models.SlugField(default='null'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='semana',
            field=models.IntegerField(blank=True, choices=[(2, 'Segunda-Feira'), (3, 'Terça-Feira'), (4, 'Quarta-Feira'), (5, 'Quinta-Feira'), (6, 'Sexta-Feira')], null=True),
        ),
    ]
