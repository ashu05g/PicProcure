# Generated by Django 3.0.7 on 2020-06-22 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_events_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_owner',
            field=models.ForeignKey(default=
            None, on_delete=django.db.models.deletion.CASCADE, to='users.Users'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='profile_pic',
            field=models.ImageField(upload_to='media'),
        ),
    ]
