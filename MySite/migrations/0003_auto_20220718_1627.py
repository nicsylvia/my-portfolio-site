# Generated by Django 3.1.1 on 2022-07-18 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0002_auto_20220709_0254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='Message',
            new_name='contact',
        ),
    ]