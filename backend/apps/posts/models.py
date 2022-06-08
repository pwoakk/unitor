from django.db import models

# Create your models here.
from backend.apps.accounts.models import User


class Posts(models.Model):
    description = models.TextField(verbose_name='Описание поста')
    image = models.ImageField(upload_to='posts/')
    create = models.TimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.TimeField(auto_now=True, verbose_name='Дата обновления')
    is_active = models.BooleanField(default=False, verbose_name='Опубликован')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-create']

    def __str__(self):
        return f'{self.user_id}'


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='comments',
        null=True
    )
    comment = models.TextField(verbose_name='Комментарий')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['-created']

    def __str__(self):
        return str(self.comment)[:50]


class Reposts(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='repost')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.TimeField(auto_now_add=True, verbose_name='Дата репоста')

    class Meta:
        verbose_name = 'Репост'
        verbose_name_plural = 'Репосты'


class PostLikes(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'



