# Generated by Django 4.0.5 on 2022-07-15 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_category_rename_position_user_pos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
