# Generated by Django 4.1.3 on 2022-12-07 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_prueba', '0026_answers_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='response',
            field=models.TextField(null=True, verbose_name='answers'),
        ),
    ]
