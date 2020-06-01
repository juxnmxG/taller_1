from django.db import models

class Pregunta(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    slug = models.SlugField()

    def _str_(self):
        return self.title
