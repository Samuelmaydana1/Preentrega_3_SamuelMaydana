from django.db import models
from django.contrib.auth.models import User
import os

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.ImageField(upload_to='avatares')
    class Meta:
        unique_together = ('user',)
    
    def __str__(self):
        return f"{self.user} - {self.imagen.url if self.imagen else 'Sin imagen'}"
    
    def save(self, *args, **kwargs):
        # Si ya existe un avatar y la imagen está cambiando, elimina el archivo viejo
        if self.pk:
            old_avatar = Avatar.objects.get(pk=self.pk)
            if old_avatar.imagen and old_avatar.imagen != self.imagen:
                if os.path.isfile(old_avatar.imagen.path):
                    os.remove(old_avatar.imagen.path)

        super().save(*args, **kwargs)

