# Generated by Django 4.1.3 on 2022-12-07 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_prueba', '0027_alter_answers_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='response',
            field=models.TextField(blank=True, null=True, verbose_name='answers'),
        ),
    ]
