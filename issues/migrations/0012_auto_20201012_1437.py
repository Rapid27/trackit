# Generated by Django 3.1.1 on 2020-10-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0011_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
