from django.db import models

# Create your models here.


class Penguin_Prediction(models.Model):
    island = models.FloatField()
    bill_length_mm = models.FloatField()
    bill_depth_mm = models.FloatField()
    flipper_length_mm = models.FloatField()
    body_mass_g = models.FloatField()
    sex = models.FloatField()
    species = models.FloatField()