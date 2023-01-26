from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

class Place(models.Model):
    text = models.TextField('Место работы')
    history = HistoricalRecords()
    
    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return f'/place/{self.id}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

class Category(models.Model):
    name = models.TextField('Название категории' , max_length=50)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/category/{self.id}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Articl(models.Model):
    title = models.CharField('Название' , max_length=50)
    info = models.CharField('Информация' , max_length=250)
    full_text = models.TextField('Текст')
    is_published = models.BooleanField(default = True , verbose_name = 'Публикация')
    data = models.DateTimeField('Дата публикации')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", blank=True, null=True, related_name="cat_Category")
    place_of_job = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место работы", blank=True, null=True, related_name="place_Job")
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/vacanse/{self.id}'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-data']

class Comments(models.Model):
    article = models.ForeignKey(Articl, on_delete=models.CASCADE, verbose_name="Вакансия", blank=True, null=True, related_name="comments_Articl")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария", blank=True, null=True)
    data = models.DateTimeField('Дата публикации', auto_now=True)
    text = models.TextField('Текст комментария')
    status = models.BooleanField('Видимость отзыва', default=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return f'/comment/{self.id}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['-data']

class Reviews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор отзыва", blank=True, null=True)
    data = models.DateTimeField('Дата публикации', auto_now=True)
    text = models.TextField('Текст отзыва')
    history = HistoricalRecords()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return f'/reviews/{self.id}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-data']

class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор новой статьи", blank=True, null=True)
    data = models.DateTimeField('Дата публикации', auto_now=True)
    text = models.TextField('Текст новости')
    history = HistoricalRecords()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-data']


