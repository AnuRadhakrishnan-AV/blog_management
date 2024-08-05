# Generated by Django 5.0.7 on 2024-08-04 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_post_author_remove_post_categories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='app1.category'),
        ),
    ]
