# Generated by Django 4.2.4 on 2023-10-12 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0025_tbl_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_rating',
            name='shop',
        ),
    ]
