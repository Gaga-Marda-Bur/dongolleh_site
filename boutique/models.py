from django.db import models


class BackgroundImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='backgrounds/')
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Image {self.id}"


class Bague(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='bagues/')

    def __str__(self):
        return self.nom
