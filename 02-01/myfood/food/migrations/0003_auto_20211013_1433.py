# Generated by Django 3.2.8 on 2021-10-13 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20211013_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pesanan',
            old_name='jumlah_pesanan_makanan',
            new_name='harga',
        ),
        migrations.RemoveField(
            model_name='pesanan',
            name='nama_makanan',
        ),
        migrations.RemoveField(
            model_name='pesanan',
            name='nama_minuman',
        ),
        migrations.AddField(
            model_name='pesanan',
            name='jenis',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pesanan',
            name='nama',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pesanan',
            name='np',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
