# Generated by Django 4.1.1 on 2023-10-10 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0017_delete_tbl_reply'),
        ('User', '0020_delete_tbl_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratingdata', models.IntegerField()),
                ('opinion', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_shop')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_newuser')),
            ],
        ),
    ]
