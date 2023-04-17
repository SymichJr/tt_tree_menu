from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    parent = models.ForeignKey('self', nul=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("menu_item", args=[self.pk])
    