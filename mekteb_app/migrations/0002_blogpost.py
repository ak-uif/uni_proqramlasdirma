from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("mekteb_app", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Başlıq")),
                ("slug", models.SlugField(allow_unicode=True, max_length=220, unique=True)),
                ("content", models.TextField(verbose_name="Mətn")),
                ("image", models.ImageField(blank=True, null=True, upload_to="blog/", verbose_name="Şəkil")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Dərc tarixi")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")),
                ("is_published", models.BooleanField(default=True, verbose_name="Dərc olunub")),
            ],
            options={
                "verbose_name": "Bloq yazısı",
                "verbose_name_plural": "Bloq yazıları",
                "ordering": ["-created_at", "-id"],
            },
        ),
    ]
