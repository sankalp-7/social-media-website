# Generated by Django 4.1.5 on 2023-03-10 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]
