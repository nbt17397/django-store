# Generated by Django 4.0.5 on 2022-07-18 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_alter_user_manager_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.department'),
        ),
    ]
