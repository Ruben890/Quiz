# Generated by Django 4.1.3 on 2022-12-13 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_prueba', '0035_remove_resuls_quetions_resuls_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forms',
            name='complete',
        ),
        migrations.AddField(
            model_name='forms',
            name='total_score_question',
            field=models.IntegerField(default=0, verbose_name='required points'),
        ),
    ]
