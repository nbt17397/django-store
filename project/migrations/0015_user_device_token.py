# Generated by Django 4.0.5 on 2022-07-18 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_alter_user_department_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='device_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
