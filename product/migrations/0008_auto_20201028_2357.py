# Generated by Django 2.2 on 2020-10-28 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20201028_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tdtcolor',
            name='id_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.CdtProductPhoto'),
        ),
    ]
