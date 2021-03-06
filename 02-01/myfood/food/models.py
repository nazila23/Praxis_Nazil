from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
# Create your models here.
class makanan(models.Model):
    np = models.TextField(max_length=200)
    menu =models.CharField(max_length=200)
    jenis =models.TextField(max_length=200)
    nama =models.TextField(max_length=200)
    harga =models.IntegerField()
    

class minuman(models.Model):
    np = models.TextField(max_length=200)
    jenis = models.TextField(max_length=200)
    nama = models.TextField()
    harga = models.IntegerField()
   

class pesanan(models.Model):
    nama_makanan = models.ForeignKey(makanan, on_delete=models.CASCADE)
    jumlah_pesanan_makanan = models.IntegerField()
    nama_minuman = models.ForeignKey(minuman, on_delete=models.CASCADE)
    jumlah_pesanan_minuman = models.IntegerField()
