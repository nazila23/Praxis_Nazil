# Generated by Django 3.2.8 on 2021-10-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20211013_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesanan',
            name='np',
        ),
        migrations.AddField(
            model_name='minuman',
            name='np',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
