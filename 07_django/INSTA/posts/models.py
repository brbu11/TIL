from django.db import models
from faker import Faker

# import os
#
# ENV = os.environ.get('ENVIRONMENT', 'development')
# if ENV == 'development':

# Create your models here.

faker = Faker()


class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            cls.objects.create(content=faker.text(120))
