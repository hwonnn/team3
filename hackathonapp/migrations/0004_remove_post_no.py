# Generated by Django 4.2.3 on 2023-07-31 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathonapp', '0003_post_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='no',
        ),
    ]
