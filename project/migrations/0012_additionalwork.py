# Generated by Django 4.0.5 on 2022-07-15 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_work_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('additional_name', models.CharField(max_length=200)),
                ('desc', models.TextField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('user_accept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('users_notification', models.ManyToManyField(blank=True, null=True, related_name='user_noti', to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.work')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
