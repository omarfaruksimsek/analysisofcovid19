# Generated by Django 4.0 on 2022-01-05 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('data', '0004_alter_girdi_kullanici'),
    ]

    operations = [
        migrations.AlterField(
            model_name='girdi',
            name='kullanici',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user'),
        ),
    ]