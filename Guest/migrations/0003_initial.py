# Generated by Django 4.2.4 on 2023-09-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0002_delete_tbl_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=35)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
