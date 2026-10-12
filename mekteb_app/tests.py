from django.contrib.admin.sites import site
from django.test import TestCase
from django.urls import reverse

from .models import BlogPost, Muellim, Telebe


class PortalTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.teacher = Muellim.objects.create(ad="Aysel", soyad="Məmmədova", fenn="Riyaziyyat")
        cls.student = Telebe.objects.create(ad="Elvin", soyad="Əliyev", qrup="A1", muellim=cls.teacher)
        cls.published = BlogPost.objects.create(title="Məktəb xəbəri", slug="mekteb-xeberi", content="Yeni yazı", is_published=True)
        cls.hidden = BlogPost.objects.create(title="Qaralama", slug="qaralama", content="Gizli yazı", is_published=False)

    def test_home_counts_only_published_posts(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["teacher_count"], 1)
        self.assertEqual(response.context["student_count"], 1)
        self.assertEqual(response.context["post_count"], 1)
        self.assertContains(response, self.published.title)
        self.assertNotContains(response, self.hidden.title)

    def test_blog_visibility_and_detail(self):
        response = self.client.get(reverse("blog"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.published.title)
        self.assertNotContains(response, self.hidden.title)
        self.assertEqual(self.client.get(reverse("blog_detail", args=[self.published.slug])).status_code, 200)
        self.assertEqual(self.client.get(reverse("blog_detail", args=[self.hidden.slug])).status_code, 404)

    def test_blog_pagination(self):
        for number in range(7):
            BlogPost.objects.create(title=f"Yazı {number}", slug=f"yazi-{number}", content="Mətn")
        first = self.client.get(reverse("blog"))
        second = self.client.get(reverse("blog"), {"page": 2})
        self.assertEqual(len(first.context["page_obj"]), 6)
        self.assertEqual(len(second.context["page_obj"]), 2)

    def test_people_and_legacy_page(self):
        for name in ("teachers", "students", "akif"):
            response = self.client.get(reverse(name))
            self.assertEqual(response.status_code, 200)
            if name != "students":
                self.assertContains(response, self.teacher.ad)
            if name != "teachers":
                self.assertContains(response, self.student.ad)

    def test_blog_registered_in_admin(self):
        self.assertIn(BlogPost, site._registry)
