# Generated by Django 4.2.4 on 2023-09-19 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0017_delete_tbl_reply'),
        ('User', '0014_remove_tbl_cart_booking_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_status', models.CharField(default='0', max_length=1)),
                ('status', models.CharField(default='0', max_length=1)),
                ('payment_status', models.CharField(default='0', max_length=1)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_newuser')),
            ],
        ),
    ]