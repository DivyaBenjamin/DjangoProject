# Generated by Django 4.1.1 on 2023-09-13 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=30)),
                ('cart_status', models.CharField(default='0', max_length=1)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_booking')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_products')),
            ],
        ),
    ]