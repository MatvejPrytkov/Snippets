# Generated by Django 5.0.7 on 2024-07-25 16:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_snippet_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authored_snippets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='snippet',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contributed_snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]