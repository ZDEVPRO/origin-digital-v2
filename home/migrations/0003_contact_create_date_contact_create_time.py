# Generated by Django 4.0.4 on 2022-05-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='create_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='create_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
