# Generated by Django 5.0.3 on 2024-05-12 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0002_remove_book_image_url_book_photo_alter_book_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='photo',
        ),
    ]
