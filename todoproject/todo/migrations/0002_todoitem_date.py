# Generated by Django 4.2.4 on 2023-08-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
