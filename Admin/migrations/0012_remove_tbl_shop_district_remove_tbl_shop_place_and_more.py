# Generated by Django 4.2.4 on 2023-09-04 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_alter_tbl_shop_photo_alter_tbl_shop_proof_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_shop',
            name='district',
        ),
        migrations.RemoveField(
            model_name='tbl_shop',
            name='place',
        ),
        migrations.DeleteModel(
            name='tbl_newuser',
        ),
        migrations.DeleteModel(
            name='tbl_shop',
        ),
    ]
