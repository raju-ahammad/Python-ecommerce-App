# Generated by Django 2.2.4 on 2019-08-22 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20190822_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Mens Jeans', 'Mens Jeans'), ('Mens Tshirt', 'Mens Tshirt'), ('Mens Watch', 'Mens Watch'), ('MEN’S SNEAKER', 'MEN’S SNEAKER'), ('WoMens Jeans', 'WoMens Jeans'), ('WoMens Tshirt', 'WoMens Tshirt'), ('WoMens Watch', 'WoMens Watch'), ('WoMens Parse', 'WoMens Parse'), ('WOMEN’S SNEAKER', 'WOMEN’S SNEAKER')], max_length=120),
        ),
    ]
