from django.contrib import admin
from preguntas.models import Pregunta

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}

admin.site.register(Pregunta, PostAdmin)
