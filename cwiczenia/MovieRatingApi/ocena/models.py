from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator



class Actor_Director(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

class Film(models.Model):
    nazwa = models.CharField(max_length=200, unique = True)
    slug = models.SlugField(max_length=200, unique=True)
    opis = models.TextField()
    aktorzy_rez = models.ManyToManyField(Actor_Director)
    srednia_ocena = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def publish(self):
        self.updated = timezone.now()
        self.save()
    
    def save(self, *args, **kwargs):
        # Obliczanie średniej oceny dla filmu
        oceny = Ocenka.objects.filter(m=self)
        suma_ocen = sum([ocena.wartosc for ocena in oceny])
        liczba_ocen = oceny.count()
        self.srednia_ocena = suma_ocen / liczba_ocen if liczba_ocen > 0 else 0.0
        super().save(*args, **kwargs)
    
    def __str__(self):
            return self.nazwa

class Ocenka(models.Model):
    m = models.ForeignKey(Film, on_delete = models.CASCADE)
    wartosc = models.FloatField(
        validators = [MinValueValidator(1), MaxValueValidator(10)]
    )
    user = models.CharField(max_length=15, unique = True)

    def __str__(self):
        return f'{self.m} {self.wartosc} {self.user}'
# Create your models here.
