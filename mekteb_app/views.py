from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import BlogPost, Muellim, Telebe


def home(request):
    return render(request, "index.html", {
        "teacher_count": Muellim.objects.count(),
        "student_count": Telebe.objects.count(),
        "post_count": BlogPost.objects.filter(is_published=True).count(),
        "latest_posts": BlogPost.objects.filter(is_published=True)[:3],
    })


def blog(request):
    posts = BlogPost.objects.filter(is_published=True)
    page_obj = Paginator(posts, 6).get_page(request.GET.get("page"))
    return render(request, "blog.html", {"page_obj": page_obj})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, "blog_detail.html", {"post": post})


def about(request):
    return render(request, "about.html")


def teachers(request):
    return render(request, "teachers.html", {"muellimler": Muellim.objects.all()})


def students(request):
    students_qs = Telebe.objects.select_related("muellim").all()
    return render(request, "students.html", {"telebeler": students_qs})


def akif_sayti(request):
    # Mövcud səhifə və kontekst açarları saxlanılır.
    context = {
        "muellimler": Muellim.objects.all(),
        "telebeler": Telebe.objects.select_related("muellim").all(),
    }
    return render(request, "akif.html", context)
