from django.db import models



class QR(models.Model):
    image = models.ImageField(upload_to='qr/')

    def __str__(self):
        return self.image.name

