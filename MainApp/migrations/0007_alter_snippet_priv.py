# Generated by Django 5.0.7 on 2024-07-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_remove_snippet_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='priv',
            field=models.CharField(choices=[('True', 'Private'), ('False', 'Public')], max_length=30, null=True),
        ),
    ]
