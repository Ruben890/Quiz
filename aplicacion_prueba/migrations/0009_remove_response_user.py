# Generated by Django 4.1 on 2022-12-02 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_prueba', '0008_alter_question_options_alter_response_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='user',
        ),
    ]
