# Generated by Django 4.1.3 on 2022-12-02 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_prueba', '0012_alter_forms_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forms',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='form',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='forms_question', to='aplicacion_prueba.forms'),
            preserve_default=False,
        ),
    ]
