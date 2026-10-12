from django.db import models

class Muellim(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    fenn = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ad} {self.soyad}"

class Telebe(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    qrup = models.CharField(max_length=20)
    muellim = models.ForeignKey(Muellim, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.ad} {self.soyad}"