# Generated by Django 3.1 on 2020-08-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_services_bought'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='deadline',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
