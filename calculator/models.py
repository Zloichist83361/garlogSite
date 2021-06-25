from django.db import models

# Create your models here.
class Calculate(models.Model):
    cityto = models.CharField(max_length=255, blank=False)
    cityfrom = models.CharField(max_length=255, blank=False)
    weightto = models.CharField(max_length=255, blank=False, default='')
    weightfrom = models.CharField(max_length=255, blank=False, default='')
    inter_terminal = models.CharField(max_length=255, blank=False)
    pickup = models.CharField(max_length=255, blank=False)
    cargo_delivery = models.CharField(max_length=255, blank=False)
    premium = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.cityto



class Term(models.Model):
    cityto = models.CharField(max_length=255, blank=False)
    cityfrom = models.CharField(max_length=255, blank=False)
    term_standart_to = models.CharField(max_length=255, blank=False)
    term_standart_from = models.CharField(max_length=255, blank=False)
    term_express_to = models.CharField(max_length=255, blank=False)
    term_express_from = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.cityto


