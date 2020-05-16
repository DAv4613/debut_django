# Generated by Django 3.0.5 on 2020-05-04 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20200503_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger'), ('W', 'warning')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]