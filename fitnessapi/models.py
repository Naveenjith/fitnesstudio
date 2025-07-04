from django.db import models

class FitnessClass(models.Model):
    name=models.CharField(max_length=50)
    instructor=models.CharField(max_length=50)
    datetime=models.DateTimeField()
    total_slots=models.PositiveIntegerField()
    available_slots=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}-{self.datetime}"
    
class ClassBooking(models.Model):
    fitness_class=models.ForeignKey(FitnessClass,on_delete=models.CASCADE)
    client_name=models.CharField(max_length=50)
    client_email=models.EmailField()

    def __str__(self):
        return f"{self.client_email}-{self.fitness_class}"