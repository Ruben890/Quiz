# Generated by Django 4.1.3 on 2022-12-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_prueba', '0019_alter_profile_total_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='time',
            field=models.IntegerField(default=0, verbose_name='time'),
        ),
    ]
