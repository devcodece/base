# Generated by Django 2.2 on 2020-10-26 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201017_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdtsize',
            name='id_product_color',
            field=models.ManyToManyField(to='product.TdtColor'),
        ),
    ]
