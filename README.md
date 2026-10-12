# Məktəb İdarəetmə Sistemi — Django

Bu layihə universitetin proqramlaşdırma dərsi çərçivəsində Python və Django istifadə edilərək hazırlanmışdır.

Layihənin əsas məqsədi verilənlər bazası ilə işləməyi, Django ORM sistemini, modellər arasında əlaqə qurmağı və məlumatların veb səhifədə göstərilməsini praktik şəkildə öyrənməkdir.

## İstifadə olunan texnologiyalar

- **Python** — Backend proqramlaşdırma dili
- **Django** — Python veb framework
- **SQLite3** — Verilənlər bazası
- **HTML** — Veb səhifənin strukturu
- **Visual Studio Code** — Kod redaktoru
- **Git və GitHub** — Versiya nəzarəti

## Layihənin funksiyaları

- Müəllim məlumatlarının bazada saxlanılması
- Tələbə məlumatlarının bazada saxlanılması
- Müəllim və tələbələr arasında əlaqənin yaradılması
- Django Admin paneli vasitəsilə məlumatların idarə edilməsi
- Bazadakı məlumatların HTML cədvəllərində göstərilməsi
- Django ORM vasitəsilə bazadan məlumatların əldə edilməsi

## Verilənlər bazasının strukturu

**Müəllim modeli (`Muellim`)**

- `ad` — Müəllimin adı
- `soyad` — Müəllimin soyadı
- `fenn` — Tədris etdiyi fənn

**Tələbə modeli (`Telebe`)**

- `ad` — Tələbənin adı
- `soyad` — Tələbənin soyadı
- `qrup` — Tələbənin qrupu
- `muellim` — Tələbənin müəllimlə əlaqəsi

Modellər arasında `ForeignKey` istifadə edilərək One-to-Many (birin-çoxa) əlaqəsi qurulmuşdur.

## Layihənin iş prinsipi

1. Modellər `models.py` faylında yaradılır.
2. Miqrasiyalar vasitəsilə verilənlər bazasında cədvəllər formalaşdırılır.
3. Django Admin panelindən məlumatlar daxil edilir.
4. `views.py` faylında ORM sorğuları ilə məlumatlar əldə olunur.
5. Əldə edilən məlumatlar HTML şablonuna ötürülür.
6. Məlumatlar veb səhifədə cədvəl şəklində göstərilir.

## Layihənin lokal işə salınması

Repository-ni klonlayın:

```bash
git clone https://github.com/ak-uif/uni_proqramlasdirma.git
```

Layihə qovluğuna daxil olun və virtual mühit yaradın:

```bash
python -m venv venv
```

Windows-da virtual mühiti aktivləşdirin:

```powershell
.\venv\Scripts\activate
```

Django paketini quraşdırın:

```bash
pip install django
```

`manage.py` faylının yerləşdiyi qovluqda miqrasiyaları tətbiq edin:

```bash
python manage.py migrate
```

Serveri başladın:

```bash
python manage.py runserver
```

Brauzerdə aşağıdakı ünvanlardan istifadə edin:

- Ana səhifə: `http://127.0.0.1:8000/`
- Məlumatların göstərilməsi: `http://127.0.0.1:8000/akif/`
- Admin panel: `http://127.0.0.1:8000/admin/`

Admin panelindən istifadə etmək üçün superuser hesabı yaradın:

```bash
python manage.py createsuperuser
```

## Öyrənilən mövzular

- Python virtual environment
- Django layihə və tətbiq strukturu
- Django Models
- SQLite verilənlər bazası
- Django ORM və QuerySet
- ForeignKey əlaqələri
- Migrations
- Views və URL Routing
- Django Templates
- Django Admin Panel

## Gələcək inkişaf planı

Layihənin növbəti mərhələsində istifadəçi interfeysi vasitəsilə CRUD əməliyyatlarının həyata keçirilməsi planlaşdırılır:

- **Create** — Yeni məlumat əlavə etmək
- **Read** — Məlumatları görüntüləmək
- **Update** — Mövcud məlumatları redaktə etmək
- **Delete** — Məlumatları silmək

## Layihənin statusu

Layihə inkişaf mərhələsindədir. Əsas verilənlər bazası modelləri, admin paneli və məlumatların göstərilməsi funksionallığı hazırlanmışdır.

---

**Layihə növü:** Universitet proqramlaşdırma layihəsi

**Repository:** https://github.com/ak-uif/uni_proqramlasdirma
