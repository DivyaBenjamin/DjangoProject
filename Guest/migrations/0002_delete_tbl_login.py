# Generated by Django 4.2.4 on 2023-09-04 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_login',
        ),
    ]