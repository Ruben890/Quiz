# Generated by Django 4.1 on 2022-12-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_prueba', '0009_remove_response_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='create',
            field=models.TimeField(auto_now_add=True),
        ),
    ]