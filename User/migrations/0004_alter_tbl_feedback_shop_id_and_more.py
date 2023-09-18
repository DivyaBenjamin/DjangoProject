# Generated by Django 4.2.4 on 2023-09-14 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0015_tbl_shop_tbl_newuser'),
        ('User', '0003_tbl_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_feedback',
            name='shop_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_shop'),
        ),
        migrations.AlterField(
            model_name='tbl_feedback',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_newuser'),
        ),
    ]