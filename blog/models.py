from cgitb import text
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# definimos que propiedades y metodos contiene cada post

# cada vez que creemos un nuevo modelo debemos crear una plantilla sql con el comando de la terminal "python manage.py makemigrations nombre_de_la_app"
# y despues importarlo a la base de datos con el comando migrate


class Post(models.Model):
    # de la librearia para base de datos de django tomamos los metodos del objeto models para crear cada campo de la db
    author = models.ForeignKey(  # tambien importamos el objeto settings para usar el model de autor pre armado
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # para programar la fecha automaticamente importamos el objeto timezone
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
