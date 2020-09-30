from django.db import models

class Lang_Page(models.Model):
    main_title = models.CharField('Главный заголовок', max_length=15, blank=True)
    permalink = models.CharField('Ссылка', max_length=12, unique=True)

    title_1 = models.CharField('Заголовок', max_length=60, blank=True)
    content_1 = models.TextField('Текст', blank=True)

    title_2 = models.CharField('Заголовок', max_length=60, blank=True)
    content_2 = models.TextField('Текст', blank=True)

    title_3 = models.CharField('Заголовок', max_length=60, blank=True)
    content_3 = models.TextField('Текст', blank=True)

    title_4 = models.CharField('Заголовок', max_length=60, blank=True)
    content_4 = models.TextField('Текст', blank=True)

    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"