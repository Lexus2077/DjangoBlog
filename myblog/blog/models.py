from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('Заголовок поста', max_length=100)
    description = models.TextField('Описание поста')
    author = models.CharField('Автор', max_length=50)
    date = models.DateField('Дата создания')
    image = models.ImageField('Изображение', upload_to='images/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
