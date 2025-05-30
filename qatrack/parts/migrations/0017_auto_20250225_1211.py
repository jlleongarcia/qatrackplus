# Generated by Django 2.2.18 on 2025-02-25 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0016_auto_20210127_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=31, verbose_name='phone number'),
        ),
        migrations.AlterUniqueTogether(
            name='partsuppliercollection',
            unique_together={('part', 'supplier', 'part_number')},
        ),
    ]
