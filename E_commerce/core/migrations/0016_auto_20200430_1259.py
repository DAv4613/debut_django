# Generated by Django 3.0.5 on 2020-04-30 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200430_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='user_id',
            new_name='user',
        ),
    ]
