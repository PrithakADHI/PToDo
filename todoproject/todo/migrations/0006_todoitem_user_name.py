# Generated by Django 4.2.4 on 2023-08-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_remove_todoitem_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='user_name',
            field=models.CharField(default='hello', max_length=200),
        ),
    ]