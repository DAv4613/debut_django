# Generated by Django 3.0.5 on 2020-05-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_remove_item_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(blank=True, choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger'), ('W', 'warning')], max_length=1, null=True),
        ),
    ]
