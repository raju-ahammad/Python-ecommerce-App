# Generated by Django 2.2.4 on 2019-08-21 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='new',
        ),
    ]
