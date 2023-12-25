from django import forms
from django.db import models


class PublishedManager(models.Manager):
    def get_is_published(self):
        return super().get_queryset().filter(is_published=News.Status.PUBLISHED)


class News(models.Model):


    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Заголовок', default=None)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug", default=None)
    photo = models.ImageField(upload_to="news_images", default=None,
                              blank=True, null=True, verbose_name='Фото')
    photo2 = models.ImageField(upload_to="products_images", default=None,
                               blank=True, null=True, verbose_name='Фото2')
    photo3 = models.ImageField(upload_to="products_images", default=None,
                               blank=True, null=True, verbose_name='Фото3')
    content = models.TextField(blank=True, verbose_name='Текст статьи', default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания', null=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения', null=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name='Статус')

    objects = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def get_view_count(self):
        """
        Возвращает количество просмотров для данной статьи
        """
        return self.views.count()




class Contact(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', default=None)
    name = models.CharField(max_length=255, verbose_name='ФИО', default=None, blank=True, null=True)
    telephone = models.CharField(max_length=30, verbose_name='Телефон', default=None, blank=True, null=True)
    faks = models.CharField(max_length=30, verbose_name='Факс', default=None, blank=True, null=True)
    email = models.EmailField(max_length=254, verbose_name='Email', null=True)
    advantage = models.IntegerField(verbose_name='Преимущество')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания', null=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения', null=True)

    class Meta:
        ordering = ['advantage']
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название должности', default=None)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug", default=None)
    duties = models.TextField(max_length=1000, verbose_name='Обязанности', default=None)
    requirements = models.TextField(max_length=1000, verbose_name='Требования к соискателю', default=None)
    offers = models.TextField(max_length=1000, verbose_name='Мы предлагаем', default=None)

    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансии'



class Tender(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', default=None)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug", default=None)
    content = models.TextField(max_length=1000000, verbose_name='Данные', default=None)

    class Meta:
        verbose_name = 'Тендеры'
        verbose_name_plural = 'Тендеры'


class Rent(models.Model):
    content = models.TextField(max_length=255, verbose_name='Данные', default=None)

    class Meta:
        verbose_name = 'Ареда'
        verbose_name_plural = 'Аренда'


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug", default=None)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории продукции'
        verbose_name_plural = 'Категории продукции'


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', default=None)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug", default=None)
    photo = models.ImageField(upload_to="products_images", default=None,
                              blank=True, null=True, verbose_name='Фото')
    photo2 = models.ImageField(upload_to="products_images", default=None,
                               blank=True, null=True, verbose_name='Фото2')
    photo3 = models.ImageField(upload_to="products_images", default=None,
                               blank=True, null=True, verbose_name='Фото3')
    content = models.TextField(blank=True, verbose_name='Описание', default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания', null=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения', null=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to="products_file",  blank=True, null=True, verbose_name='Файл')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        verbose_name = 'Продукия'
        verbose_name_plural = 'Продукия'



class Nelekvidi(models.Model):
    title = models.CharField(max_length=1, unique=True, verbose_name='Буква', default=None)
    content = models.TextField(blank=True, verbose_name='Текст', default=None)
    eng = models.CharField(max_length=3, unique=True, verbose_name='Англ ссылка', default=None)

    class Meta:
        verbose_name = 'Нелеквиды'
        verbose_name_plural = 'Нелеквиды'


class TransportBY(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', default=None)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug", default=None)
    photo = models.ImageField(upload_to="transportby_images", default=None,
                              blank=True, null=True, verbose_name='Фото')
    photo2 = models.ImageField(upload_to="transportby_images", default=None,
                               blank=True, null=True, verbose_name='Фото2')
    photo3 = models.ImageField(upload_to="transportby_images", default=None,
                               blank=True, null=True, verbose_name='Фото3')
    content = models.TextField(blank=True, verbose_name='Описание', default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания', null=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения', null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Транспорт Б/У'
        verbose_name_plural = 'Транспорт Б/У'
        ordering = ['-time_create']




class Services(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', default=None)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug", default=None)
    photo = models.ImageField(upload_to="services_images", default=None,
                              blank=True, null=True, verbose_name='Фото')
    content = models.TextField(blank=True, verbose_name='Описание', default=None)
    file = models.FileField(upload_to="services_file",  blank=True, null=True, verbose_name='Файл')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'




