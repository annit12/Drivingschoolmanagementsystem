# Generated by Django 4.1.1 on 2023-04-14 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drapp', '0006_alter_instructor_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='instructor',
        ),
    ]
