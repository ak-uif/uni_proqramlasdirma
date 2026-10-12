from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from mekteb_app import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("blog/", views.blog, name="blog"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("about/", views.about, name="about"),
    path("teachers/", views.teachers, name="teachers"),
    path("students/", views.students, name="students"),
    path("akif/", views.akif_sayti, name="akif"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
