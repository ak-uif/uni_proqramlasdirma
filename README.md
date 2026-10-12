# Məktəb portalı

Universitetin proqramlaşdırma dərsi üçün hazırlanmış layihə (`uni_proqramlasdirma`). Məqsəd Django ORM, modellər arasındakı əlaqə, miqrasiya, admin paneli və şablonlarla işləməyi praktik öyrənməkdir.

Bu mövcud Django layihəsi müəllim və tələbə məlumatlarını, məktəb haqqında ümumi məlumatı və bloq yazılarını Azərbaycan dilində təqdim edir. Əvvəlki `/akif/` səhifəsi saxlanılıb.

## Texnologiyalar

- Python, Django və Django şablonları
- PostgreSQL (`mekteb_db`)
- Pillow (bloq şəkilləri üçün)
- HTML və CSS

## İmkanlar

- Ana səhifədə bazadan hesablanan müəllim, tələbə və dərc olunmuş yazı sayı
- Son üç dərc olunmuş yazı, səhifələnən bloq və yazı səhifəsi
- Müəllim və tələbə siyahıları
- Django Admin vasitəsilə bloq yazısı və şəkil idarəetməsi
- Telefon və planşet ölçülərinə uyğun görünüş
- Mövcud `/akif/` səhifəsində müəllim və tələbə cədvəlləri

## Modellər və iş prinsipi

`Muellim` modelində ad, soyad və fənn; `Telebe` modelində ad, soyad, qrup və müəllimlə `ForeignKey` əlaqəsi saxlanılır. Bir müəllimin bir neçə tələbəsi ola bilər. `BlogPost` modelində başlıq, unikal slug, mətn, istəyə bağlı şəkil, tarixlər və dərc statusu var.

Modellər `models.py` faylında təyin olunur, miqrasiyalar PostgreSQL cədvəllərini yaradır, `views.py` içində ORM sorğuları məlumatları şablonlara ötürür. Məlumatlar Django Admin vasitəsilə idarə olunur.

## Quraşdırma

Python 3.12 və PostgreSQL serveri hazır olmalıdır. `manage.py` olan qovluqda işləyin. **PowerShell** üçün:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

PostgreSQL-də mövcud `mekteb_db` bazasını və istifadəçi hüquqlarını saxlayın. `POSTGRES_PASSWORD` mühit dəyişənini mövcud `postgres` istifadəçisinin paroluna təyin edin; parolu kodda və ya repozitoriyada saxlamayın. Məsələn, cari PowerShell sessiyasında:

```powershell
$env:POSTGRES_PASSWORD = [System.Net.NetworkCredential]::new('', (Read-Host 'PostgreSQL parolu' -AsSecureString)).Password
```

**CMD** istifadə edirsinizsə, PowerShell əmrlərini orada yazmayın. Mövcud `venv` qovluğunuz varsa, `"C:\uni lahiyesi\venv\Scripts\activate.bat"` ilə aktivləşdirin. Sonra `powershell` yazıb yuxarıdakı parol əmrini və aşağıdakı Django əmrlərini həmin PowerShell pəncərəsində icra edin.

Hazırkı layihə ayarları PostgreSQL-i `localhost:5432` ünvanında gözləyir. Bu ünvan, baza adı və ya istifadəçi fərqlidirsə, `mekteb/settings.py` içində uyğunlaşdırın. SQLite faylı bu veb sayt üçün istifadə olunmur.

## Miqrasiya və server

```powershell
python manage.py check
python manage.py migrate
python manage.py test
python manage.py runserver
```

Ana səhifə `http://127.0.0.1:8000/`, bloq `http://127.0.0.1:8000/blog/`, əvvəlki cədvəl səhifəsi `http://127.0.0.1:8000/akif/`, admin paneli `http://127.0.0.1:8000/admin/` ünvanında açılır. Admin hesabı yoxdursa, `python manage.py createsuperuser` əmrindən istifadə edin.

## Bloq idarəetməsi

Admin panelində **Bloq yazıları** bölməsindən başlıq, URL üçün unikal slug, mətn və istəyə bağlı şəkil əlavə edin. Başlıq yazıldıqda slug avtomatik doldurulur; Azərbaycan hərfləri qəbul edilir. Yazını gizlətmək üçün **Dərc olunub** seçimini söndürün. Gizli yazılar ictimai səhifələrdə görünmür.

Yüklənən şəkillər `media/blog/` qovluğunda saxlanılır. İnkişaf rejimində Django onları təqdim edir; istehsal mühitində media faylları üçün ayrıca veb server və təhlükəsiz konfiqurasiya tələb olunur.

## Öyrənilən mövzular

Virtual mühit, Django layihə strukturu, ORM və QuerySet, `ForeignKey` əlaqəsi, miqrasiyalar, URL marşrutları, şablon irsiyyəti və Django Admin.

**Repozitoriya:** https://github.com/ak-uif/uni_proqramlasdirma
