# Generated by Django 5.1.2 on 2024-11-02 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_user_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirmed',
        ),
        migrations.AddField(
            model_name='policy',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='подтвержденый'),
        ),
    ]
