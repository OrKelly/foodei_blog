from django.utils import timezone

from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from modules.services.utils import unique_slugify

class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL,
                               null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, default='')
    image = models.ImageField(upload_to='articles/', verbose_name='Изображение поста')
    text = RichTextField(verbose_name='Описание блюда')
    prep_time = models.PositiveIntegerField(default=0, verbose_name='Время на подготовку')
    cook_time = models.PositiveIntegerField(default=0, verbose_name='Время на приготовление')
    ingredients = RichTextField(verbose_name='Список инградиентов')
    directions = RichTextField(verbose_name='Действия')
    time_to_read = models.PositiveIntegerField(verbose_name='Время на чтение')
    category = models.ForeignKey(Category, related_name='post',
                                 on_delete=models.SET_NULL,
                                 null=True, verbose_name='Категория')
    tag = models.ManyToManyField(Tag, related_name='post', verbose_name='Теги')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_single', kwargs={'slug': self.category.slug, 'post_slug': self.slug})

    def get_comments(self):
        return self.comment.all()

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.title)

        self.time_to_read = int(len(list(self.text.split()))/120)
        super().save(*args, **kwargs)

# class Recipe(models.Model):
#     name = models.CharField(max_length=100)
#     serves = models.CharField(max_length=50)
#     prep_time = models.PositiveIntegerField(default=0)
#     cook_time = models.PositiveIntegerField(default=0)
#     ingredients = RichTextField()
#     directions = RichTextField()
#     post = models.ForeignKey(Post, related_name='recipe', null=True, on_delete=models.SET_NULL,
#                              blank=True)
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         """
#         Сохранение полей модели при их отсутствии заполнения
#         """
#         if not self.slug:
#             self.slug = unique_slugify(self, self.title)
#         super().save(*args, **kwargs)


class Comment(models.Model):
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name='comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.message

