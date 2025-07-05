from django.db import models

# Create your models here.

class Prediction(models.Model):
      sepal_length = models.FloatField()
      sepal_width = models.FloatField()
      petal_length = models.FloatField()
      petal_width = models.FloatField()
      predicted_class = models.IntegerField()
      timestamp = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f'Prediction: {self.predicted_class} at {self.timestamp}'
