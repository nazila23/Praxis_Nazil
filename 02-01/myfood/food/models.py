from django.db import models

# Create your models here.
class makanan(models.Model):
    np = models.TextField(max_length=200)
    menu =models.CharField(max_length=200)
    jenis = models.TextField(max_length=200)
    nama = models.TextField(max_length=200)
    harga = models.IntegerField()

class minuman(models.Model):
    np = models.TextField(max_length=200)
    jenis = models.TextField(max_length=200)
    nama = models.TextField()
    harga = models.IntegerField()

class pesanan(models.Model):
    jenis = models.TextField(max_length=200)
    nama = models.TextField(max_length=200)
    harga = models.IntegerField()