from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ward(models.Model):
    quantity = models.IntegerField()

    def __str__(self):
        return f"Ward {self.id} - Quantity: {self.quantity}"

class Patient(models.Model):
    name = models.CharField(max_length=100)
    id_ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    id_doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
