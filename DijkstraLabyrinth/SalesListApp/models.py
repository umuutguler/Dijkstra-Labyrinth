from django.db import models

# Create your models here.


class HepsiBurada(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=100)
    marka = models.CharField(max_length=100)
    model_adi = models.CharField(max_length=100)
    prices = models.IntegerField()  # it should be bettor to int field
    puani = models.CharField(max_length=100)
    ekran_boyutu = models.CharField(max_length=100)
    islemci = models.CharField(max_length=100)
    islemci_tipi = models.CharField(max_length=100)
    isletim_sistemi = models.CharField(max_length=100)
    ssd_kapasitesi = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    # Todo: Need to add computer photo
