# Generated by Django 3.1.1 on 2020-10-11 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0009_auto_20201011_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_assignee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.IntegerField(blank=3, choices=[(1, '1 - Very High'), (2, '2 - High'), (3, '3 - Medium'), (4, '4 - Low'), (5, '5 - Very Low')], default=3),
        ),
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(error_messages={'null': 'Please select a project.'}, on_delete=django.db.models.deletion.CASCADE, related_name='issue_project', to='issues.project'),
        ),
    ]
