from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="auteur")
    title = models.CharField('titre', max_length=200)
    text = models.TextField('texte')
    created_date = models.DateTimeField("date de création",default=timezone.now)
    published_date = models.DateTimeField("date de publication", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
