# Generated by Django 4.1.3 on 2022-12-08 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_prueba', '0028_alter_answers_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='points',
            field=models.IntegerField(choices=[(5, 5), (10, 10), (20, 20)], max_length=2, verbose_name='point value'),
        ),
    ]
