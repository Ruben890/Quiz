# Generated by Django 4.1.3 on 2022-12-03 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_prueba', '0014_profile_total_score_question_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='points',
            field=models.CharField(choices=[('5', '5'), ('10', '10'), ('20', '20')], max_length=2, verbose_name='puntos'),
        ),
    ]
