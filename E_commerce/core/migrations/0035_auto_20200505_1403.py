# Generated by Django 3.0.5 on 2020-05-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20200505_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, choices=[('bb', 'boubou'), ('rb', 'robe'), ('jp', 'jupe'), ('pt', 'pantalon'), ('mi', 'miel'), ('be', 'beurre'), ('ba', 'basin'), ('pagne baoule', 'pagne baoule')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='reduction',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
