# Generated by Django 2.2.3 on 2019-07-25 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='vodes',
            new_name='votes',
        ),
    ]
