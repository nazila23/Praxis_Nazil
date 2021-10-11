from django.db import models

# Create your models here.
class makanan(models.Model):
    jenis = models.TextField(max_length=200)
    nama = models.TextField()
    harga = models.IntegerField()

class minuman(models.Model):
    jenis = models.TextField(max_length=200)
    nama = models.TextField()
    harga = models.IntegerField()

class pesanan(models.Model):
    nama_makanan = models.CharField(max_length=200)
    jumlah_pesanan_makanan = models.IntegerField()
    nama_minuman = models.CharField(max_length=200)
    jumlah_pesanan_makanan = models.IntegerField()