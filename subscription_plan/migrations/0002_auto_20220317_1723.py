# Generated by Django 2.2.26 on 2022-03-17 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_plan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='tier',
        ),
        migrations.AddField(
            model_name='plan',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='price',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
