# Generated by Django 4.1 on 2022-12-02 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_prueba', '0004_response_question_forms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(default='pregunta.jpg', upload_to='', verbose_name='imagen_profile'),
        ),
    ]