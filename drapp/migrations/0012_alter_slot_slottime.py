# Generated by Django 4.1.1 on 2023-04-17 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drapp', '0011_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='slottime',
            field=models.TimeField(),
        ),
    ]