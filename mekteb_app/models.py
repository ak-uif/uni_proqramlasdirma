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


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlıq")
    slug = models.SlugField(max_length=220, unique=True, allow_unicode=True)
    content = models.TextField(verbose_name="Mətn")
    image = models.ImageField(upload_to="blog/", blank=True, null=True, verbose_name="Şəkil")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Dərc tarixi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")
    is_published = models.BooleanField(default=True, verbose_name="Dərc olunub")

    class Meta:
        ordering = ["-created_at", "-id"]
        verbose_name = "Bloq yazısı"
        verbose_name_plural = "Bloq yazıları"

    def __str__(self):
        return self.title
