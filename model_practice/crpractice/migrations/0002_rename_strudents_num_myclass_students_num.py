# Generated by Django 3.2 on 2021-04-23 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crpractice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myclass',
            old_name='strudents_num',
            new_name='students_num',
        ),
    ]