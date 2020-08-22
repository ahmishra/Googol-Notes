from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import misaka

# Create your models here.
User = get_user_model()


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)
    note = models.TextField()
    note_html = models.TextField(editable=False, default='', blank=True)
    related_tag = models.CharField(
        max_length=256, null=True, blank=True, default='No Related Tag(s)')

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kargs):
        self.note_html = misaka.html(self.note)
        super().save(*args, *kargs)

    def get_absolute_url(self):
        return reverse('app:all-notes')
