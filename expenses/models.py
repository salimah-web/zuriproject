from django.db import models
from authentication.models import User
# Create your models here.

class Expense(models.Model):
    CATEGORY_OPTIONS=[
        ('FOOD','FOOD'),
        ('RENT','RENT'),
        ('TRAVEL','TRAVEL'),
        ('OTHERS','OTHERS')
    ]

    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2, max_length= 255)
    description = models.TextField()
    owner = models.ForeignKey(to= User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)

    class Meta:
        ordering=['-date']

    def __str__(self):
        return str(self.owner)+'s expenses'
