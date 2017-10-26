from django.db import models

# Create your models here.

class Equipment(models.Model):
    name = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=50, null=True)
    sn = models.CharField(max_length=25, unique=True)
    inv = models.CharField(max_length=20, unique=True)
    exp_start_date = models.DateField() # exploitation start date
    exp_end_date = models.DateField() # exploitation end date, utilized
    broken = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Repairing(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    company = models.CharField(max_length=120, null=True) # Company that fix our equipment
    crash_date = models.DateField() # when equipment fault
    send_date = models.DateField(null=True) # when send equipment to repairing company
    return_date = models.DateField(null=True) # when company return equipment
    price = models.FloatField(null=True)
    comment = models.TextField()

    def __str__(self):
        return self.equipment.name


class Categories(models.Model):
    name = models.ManyToManyField(Equipment)

    def __str__(self):
        return self.name


class Companies(models.Model):
    name = models.ForeignKey(Repairing, on_delete=models.CASCADE)
    tel = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name