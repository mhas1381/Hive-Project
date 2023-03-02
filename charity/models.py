from django.db import models

# Create your models here.
class Advertisement(models.Model):
    raiser = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads/', default = 'ads/default.png')
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    amount = models.FloatField()
    collected_amount = models.FloatField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



