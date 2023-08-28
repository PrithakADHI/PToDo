# Generated by Django 4.2.4 on 2023-08-23 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todoitem_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='person_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
