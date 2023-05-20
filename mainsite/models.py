from django.db import models
from random import randint
from django.urls import reverse
from datetime import datetime
import django


class For_me(models.Model):
    """Модуль профиля раздала обо мне"""

    name = models.CharField(max_length=200, db_index=True,verbose_name='Название')
    photo = models.ImageField(upload_to=f'image/For_me/{randint(1,100)}', blank=True, verbose_name='Обложка')
    text = models.TextField(blank=True, verbose_name='Описание')
    avail = models.BooleanField(default=True, verbose_name='Активость')


    class Meta:
        ordering = ('name',)
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'

    def __str__(self):
        return self.name

class Partners(models.Model):

    name = models.CharField(max_length=200, db_index=True,verbose_name='Название')
    photo = models.ImageField(upload_to=f'image/Partners/{randint(1,100)}', blank=True, verbose_name='Обложка')
    avail = models.BooleanField(default=True, verbose_name='Активость')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Партнеры'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.name

class Services(models.Model):

    name = models.CharField(max_length=200,db_index=True,verbose_name='Назвение услуги')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name



class Keys(models.Model):

    name = models.CharField(max_length=200, db_index=True,verbose_name='Название кейса')
    slug = models.SlugField(max_length=200, db_index=True,verbose_name='Уникальный url (Генерируется сам)')
    logo = models.ImageField(upload_to=f'image/Keys/{randint(1,10000)}', blank=True,verbose_name='Обложка')
    price = models.IntegerField(verbose_name='Цена', blank=False, default=1)
    price_for_sale = models.IntegerField(verbose_name='Цена со скидкой',blank=True , null=True)
    description = models.TextField(blank=True,verbose_name='Краткое описание')
    text = models.TextField(blank=True, verbose_name='Полное описание')
    services = models.ManyToManyField(Services, verbose_name='Услуги')
    available = models.BooleanField(default=True,verbose_name='Активость')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Кейсы'
        verbose_name_plural = 'Кейсы'

    def __str__(self):
        return self.name

class Images_keys (models.Model):

    product = models.ForeignKey(Keys, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=f'image/Keys/{randint(1,10000)}', blank=True,verbose_name='Фото')

    class Meta:
        verbose_name = 'Дополнительное фото кейсов'
        verbose_name_plural = 'Дополнительные фото кейса'



class Zaiavki(models.Model):

    name = models.CharField(max_length=200, db_index=True,verbose_name='Имя')
    date = models.DateField(blank=True, verbose_name='Дата создания', default=django.utils.timezone.now)
    svaz = models.CharField(max_length=200,blank=True, verbose_name='Способ связи')
    description = models.TextField(blank=True, verbose_name='Описание заказа')
    status = models.TextField(blank=True, verbose_name='Стастус заявки')
    available = models.BooleanField(default=True,verbose_name='Активость')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name



class Nevs(models.Model):

    name = models.CharField(max_length=200, db_index=True,verbose_name='Имя')
    date = models.DateField(blank=True, verbose_name='Дата создания',default=django.utils.timezone.now)
    logo = models.ImageField(upload_to=f'image/Nevs/{randint(1, 10000)}', blank=True, verbose_name='Обложка')
    main_text = models.TextField(blank=True, verbose_name='Текст новости')
    available = models.BooleanField(default=True,verbose_name='Активость')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Новсть'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.name

class Images_nevs (models.Model):

    product = models.ForeignKey(Nevs, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=f'image/Keys/{randint(1,10000)}', blank=True,verbose_name='Фото')

    class Meta:

        verbose_name = 'Дополнительное фото новостей '
        verbose_name_plural = 'Дополнительные фото новости'

class Contakts(models.Model):

    name = models.CharField(max_length=200,blank=True, verbose_name='Название')
    url = models.CharField(max_length=500,blank=True, verbose_name='Ссылка')
    available = models.BooleanField(default=True, verbose_name='Активость')

    class Meta:

        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name

