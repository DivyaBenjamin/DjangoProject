# Generated by Django 4.2.4 on 2023-08-31 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_tbl_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
    ]
