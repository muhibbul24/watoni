# Generated by Django 4.1.7 on 2023-04-04 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ximage',
            name='uploader',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]