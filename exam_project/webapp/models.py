from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='info', verbose_name='Пользователь')
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Телефон')
    friends = models.ManyToManyField(User, null=True, blank=True, verbose_name='Друзья')
    avatar = models.ImageField(null=True, blank=True, verbose_name='Фотография')

    def __str__(self):
        return self.user.get_full_name()


class Post(models.Model):
    autor = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='post', verbose_name='Автор')
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(max_length=5000, null=False, blank=False, verbose_name='Текст')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return '%s: %s' % (self.pk, self.title)
