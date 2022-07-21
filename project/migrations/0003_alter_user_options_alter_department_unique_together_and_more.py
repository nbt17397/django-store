# Generated by Django 4.0.5 on 2022-07-15 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_user_address_user_department_id_user_ispm_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together={('manager', 'department_name')},
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('email', 'department_id')},
        ),
    ]