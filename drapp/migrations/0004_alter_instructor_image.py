# Generated by Django 4.1.1 on 2023-03-14 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drapp', '0003_remove_student_photo_instructor_image_student_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='image',
            field=models.ImageField(default='', upload_to='drapp/static/img'),
        ),
    ]