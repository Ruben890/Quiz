# Generated by Django 4.1.3 on 2022-12-03 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_prueba', '0018_alter_profile_total_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='total_score',
            field=models.IntegerField(default=0, verbose_name='total_score'),
        ),
    ]
