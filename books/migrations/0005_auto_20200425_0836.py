# Generated by Django 3.0.5 on 2020-04-25 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
