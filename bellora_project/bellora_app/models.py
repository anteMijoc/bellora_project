from django.db import models

class Kategorija(models.Model):
    naziv = models.CharField(max_length=100)
    def __str__(self):
        return self.naziv

class Proizvod(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    slika = models.ImageField(upload_to='proizvodi/')
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)
    def __str__(self):
        return self.naziv