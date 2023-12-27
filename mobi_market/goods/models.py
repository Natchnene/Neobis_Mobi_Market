from django.db import models
from users.models import User


class CardProduct(models.Model):
    title = models.CharField(max_length=200, blank=False)
    price = models.PositiveIntegerField(blank=False)
    photo = models.ImageField(null=True, blank=True)
    short_description = models.CharField(max_length=200, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_card_products', blank=True)

    def all_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"id: {self.pk} - user_id: {self.user_id} - title{self.title}"

