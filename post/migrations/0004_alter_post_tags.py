# Generated by Django 4.1.5 on 2023-02-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_stream_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='tags', to='post.tag'),
        ),
    ]
