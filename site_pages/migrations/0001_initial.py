# Generated by Django 3.0.6 on 2020-06-22 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lang_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(blank=True, max_length=15, verbose_name='Главный заголовок')),
                ('permalink', models.CharField(max_length=12, unique=True, verbose_name='Ссылка')),
                ('title_1', models.CharField(blank=True, max_length=60, verbose_name='Заголовок')),
                ('content_1', models.TextField(blank=True, verbose_name='Текст')),
                ('title_2', models.CharField(blank=True, max_length=60, verbose_name='Заголовок')),
                ('content_2', models.TextField(blank=True, verbose_name='Текст')),
                ('title_3', models.CharField(blank=True, max_length=60, verbose_name='Заголовок')),
                ('content_3', models.TextField(blank=True, verbose_name='Текст')),
                ('title_4', models.CharField(blank=True, max_length=60, verbose_name='Заголовок')),
                ('content_4', models.TextField(blank=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
