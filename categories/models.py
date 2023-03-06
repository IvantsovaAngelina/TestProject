from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    pay = models.IntegerField(max_length=50)
    image = models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return self.title
