# Generated by Django 3.0.2 on 2020-01-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni_user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]