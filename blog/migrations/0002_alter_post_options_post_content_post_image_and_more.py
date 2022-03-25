# Generated by Django 4.0 on 2022-01-13 00:24

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish_date', 'id']},
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=datetime.datetime(2022, 1, 13, 0, 23, 41, 623860, tzinfo=utc), verbose_name='İçerik'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
        migrations.AddField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Yayın Tarihi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, editable=False, max_length=130, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=2019, max_length=120, verbose_name='Başlık'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='auth.user'),
        ),
    ]