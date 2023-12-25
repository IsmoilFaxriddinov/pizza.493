from django.db import models

# Create your models here.

class ScrollModel(models.Model):
    image = models.ImageField(upload_to="scrolls")
    discount = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updadet_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "scroll"
        verbose_name_plural = "scrolls"


class GaleryModel(models.Model):
    image = models.ImageField(upload_to="galery/")
    created_at = models.DateTimeField(auto_now_add=True)
    updadet_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.image
    
    class Meta:
        verbose_name = "galery"
        verbose_name_plural = "galeries"
