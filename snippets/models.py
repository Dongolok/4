from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    imgpath = models.CharField(max_length=200)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)
    logo = models.CharField(max_length=200)


class Branch(models.Model):
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    branch = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branches', default=True)


class Contact(models.Model):
    CONTACT_CHOICES = [
        (1, 'Facebook'),
        (2, 'Phone'),
        (3, 'Email'),
    ]

    type = models.CharField(
        max_length=2,
        choices=CONTACT_CHOICES,
        default=True,
    )

    contact = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contacts', default=True)
    value = models.CharField(max_length=200)



