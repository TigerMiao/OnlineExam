# Generated by Django 2.1 on 2018-08-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
