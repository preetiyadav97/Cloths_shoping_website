# Generated by Django 4.2.5 on 2023-09-18 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Buy', '0009_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, max_length=254, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
