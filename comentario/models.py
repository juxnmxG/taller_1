from django.db import models
from django.conf import settings

class  Comentario(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    contenido = models.TextField()
    autor = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE,
    related_name = 'comments'
    )


    def _str_(self):
        return self.contenido[:20]
