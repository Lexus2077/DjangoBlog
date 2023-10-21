# Generated by Django 4.2.6 on 2023-10-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок поста')),
                ('description', models.TextField(verbose_name='Описание поста')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('date', models.DateField(verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]