# Generated by Django 4.1.1 on 2023-05-07 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drapp', '0018_alter_bookslot_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='image2',
            field=models.ImageField(default='', upload_to='media/instructors/'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='image3',
            field=models.ImageField(default='', upload_to='media/instructors/'),
        ),
    ]
