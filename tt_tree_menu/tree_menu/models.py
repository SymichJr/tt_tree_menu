from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("menu_item", args=[self.pk])
    
    def get_children(self):
        return MenuItem.objects.select_related(parent=self)
    