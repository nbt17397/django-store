# Generated by Django 4.0.5 on 2022-07-15 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_process_alter_boxchat_users_alter_project_users_work_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.category'),
        ),
    ]
