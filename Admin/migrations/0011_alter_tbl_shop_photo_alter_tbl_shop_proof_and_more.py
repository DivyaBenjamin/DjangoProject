# Generated by Django 4.2.4 on 2023-09-04 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_delete_tbl_newuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_shop',
            name='photo',
            field=models.FileField(upload_to='Shopphoto/'),
        ),
        migrations.AlterField(
            model_name='tbl_shop',
            name='proof',
            field=models.FileField(upload_to='Shopproof/'),
        ),
        migrations.CreateModel(
            name='tbl_newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('contact', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=55)),
                ('gender', models.CharField(max_length=45)),
                ('photo', models.FileField(upload_to='Userphoto/')),
                ('password', models.CharField(max_length=45)),
                ('conpassword', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_district')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
