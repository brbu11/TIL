from django.db import models
from faker import Faker

faker = Faker()


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=30)

    # class Meta:
    #     ordering = ('name',)
    #
    # @classmethod
    # def dummy(cls, n):
    #     for i in range(n):
    #         cls.objects.create(name=faker.name())


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    clients = models.ManyToManyField(Client)

    # @classmethod
    # def dummy(cls, n):
    #     for i in range(n):
    #         cls.objects.create(name=faker.company())


class Student(models.Model):
    name = models.CharField(max_length=30)


class Lecture(models.Model):
    title = models.CharField(max_length=100)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, default='')
