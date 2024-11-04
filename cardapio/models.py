from django.db import models
from django.utils.text import slugify

# Create your models here.


SEMANA = {
    2: "Segunda-Feira",
    3: "Terça-Feira",
    4: "Quarta-Feira",
    5: "Quinta-Feira",
    6: "Sexta-Feira",
}

class Cardapio(models.Model):
    img = models.ImageField()
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    semana = models.IntegerField(choices=SEMANA)
    slug = models.SlugField(blank=True, null=False, unique=True)
    
    def __str__(self):
        return SEMANA[self.semana]
    
    def save(self, **kwargs):
        self.slug = slugify(SEMANA[self.semana])
        return super().save(**kwargs)