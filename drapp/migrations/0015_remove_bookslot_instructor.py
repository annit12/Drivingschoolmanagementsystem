# Generated by Django 4.1.1 on 2023-04-17 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drapp', '0014_bookslot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookslot',
            name='Instructor',
        ),
    ]
