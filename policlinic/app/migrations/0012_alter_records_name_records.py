# Generated by Django 5.1.2 on 2024-11-01 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_records_date_create_alter_records_date_record_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='name_records',
            field=models.CharField(default='Запись', max_length=100),
        ),
    ]