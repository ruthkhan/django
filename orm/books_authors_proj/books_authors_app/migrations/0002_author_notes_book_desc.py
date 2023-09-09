# Generated by Django 4.2.4 on 2023-09-08 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='to be updated'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(default='to be updated'),
            preserve_default=False,
        ),
    ]
