from django.db import models

class Resume_Model(models.Model):
    photo = models.ImageField(upload_to="gallery")