# Generated by Django 3.0.4 on 2020-03-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='descricao',
            field=models.TextField(default='', max_length=200, verbose_name='Descrição'),
        ),
    ]