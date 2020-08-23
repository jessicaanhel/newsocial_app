# Generated by Django 3.1 on 2020-08-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20200823_0749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'PLN'},
        ),
        migrations.RemoveField(
            model_name='basket',
            name='buyer',
        ),
        migrations.AlterField(
            model_name='services',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='PLN'),
        ),
    ]