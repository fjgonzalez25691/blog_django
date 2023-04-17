from django.db import models

class FavoriteManager(models.Manager):
    
    def entradas_user(self, usuario):
        #return super().get_queryset().filter(
        return self.filter(
            entry__public__isnull = False,
            user=usuario
        ).order_by('-created')
    
