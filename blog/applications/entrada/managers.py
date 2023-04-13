from django.db import models

class EntryManager(models.Manager):
    '''Procedimento para entrada'''
    def entrada_en_portada(self):
        return self.filter(
            public__isnull=False,
            portada=True
        # accedemos a la fecha de creación porque ya viene en el
        # TimeStampedModel aunque no la hayamos creado específicamente
        ).order_by('-created').first()
        
    def entradas_en_home(self):
        #devuelve las últimas cuatro entradas 
        return self.filter(
            in_home=True,
        ).order_by('-created')[:4]
        
    def entradas_recientes(self):
        #devuelve las últimas 6 entradas
        return self.filter(
            in_home=True,      
        ).order_by('-created')[:6]
    
    def todos_las_entradas(self):
        return self.all()
    
    def prueba(self):
        return self.filter(
            public__isnull=False,
            portada=True
        # accedemos a la fecha de creación porque ya viene en el
        # TimeStampedModel aunque no la hayamos creado específicamente
        ).order_by('-created').first()
