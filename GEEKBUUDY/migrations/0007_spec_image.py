# Generated by Django 2.2.7 on 2019-11-30 18:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GEEKBUUDY', '0006_auto_20191130_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='spec',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/'),
            preserve_default=False,
        ),
    ]
