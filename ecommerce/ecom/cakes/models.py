from django.db import models
from django.urls import reverse
from django.shortcuts import redirect
from django.core.validators import MaxValueValidator, MinValueValidator
from utils.slugs import said_slug
from django.contrib.auth.models import User


class Cake(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=1000)
    weight = models.PositiveIntegerField(default=0, help_text="in grams")
    price = models.FloatField(default=0, help_text="AZN")
    baked_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d", null=True, blank=True)
    stars = models.FloatField(default=0, null=True, blank=True, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    slug = models.SlugField(max_length=64, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.price}AZN"
    
    def save(self, *args, **kwargs):
        self.slug = said_slug(self.name)
        return super(Cake, self).save(*args, **kwargs)
    
    def get_absolute_url(self) -> str:
        return reverse("cakes:details", kwargs= {
            "pk": self.pk,
            "slug": self.slug})

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self) -> str:
        return str(self.user)
    
class Post(models.Model):
    title = models.CharField(max_length=32)
    header_image = models.ImageField(upload_to="photos/%Y/%m/%d", null=True, blank=True)
    title_tag = models.CharField(max_length=100)
    #author = models.ForeignKey(User, default=None)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
