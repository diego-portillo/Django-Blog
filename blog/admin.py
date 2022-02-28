from django.contrib import admin
# con esto importamos el modelo que puede ser vinculado a un admin
from .models import Post
# Register your models here.
# esta linea de codigo crea el vinculo admin-post para que el admin pueda modificar los posteos y le hacemos visible en la vista de admin
admin.site.register(Post)
