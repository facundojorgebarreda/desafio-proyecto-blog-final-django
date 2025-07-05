from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    body = RichTextField()
    image = models.ImageField(upload_to="pages", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
