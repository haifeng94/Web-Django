# Generated by Django 2.1.7 on 2019-03-21 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_counts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag_name',
            new_name='name',
        ),
    ]
