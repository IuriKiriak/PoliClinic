# Generated by Django 5.1.2 on 2024-11-01 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_policy_options_alter_specialization_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='date_record',
            field=models.DateField(default=None),
        ),
    ]