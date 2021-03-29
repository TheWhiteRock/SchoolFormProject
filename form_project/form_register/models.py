from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

class Form(models.Model):
    fullname = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=3, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)


class Principal(models.Model):
    fullname = models.CharField(max_length=100, null=True, blank=True )
    message = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=3, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
class Teacher(models.Model):
    fullname = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=3, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
class Student(models.Model):
    fullname = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=3, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)