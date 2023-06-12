from django.db import models

# Create your models here.
GENDER_CHOICES =(
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

class signup_form(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=255, choices = GENDER_CHOICES)
    address = models.TextField()
    experience = models.DecimalField(max_digits=3, decimal_places=2)
    resume = models.FileField()

    def __str__(self):
        return self.name