# Generated by Django 3.1.5 on 2021-03-01 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210301_0811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='tipo',
        ),
    ]
