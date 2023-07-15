# Generated by Django 4.2 on 2023-04-08 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_ximage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='ximage',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ximage',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
