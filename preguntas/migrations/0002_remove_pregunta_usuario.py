# Generated by Django 2.0.1 on 2020-06-01 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='usuario',
        ),
    ]
