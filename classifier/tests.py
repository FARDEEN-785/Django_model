from django.test import TestCase
from .models import Prediction

# Create your tests here.

#Testing + Deployment
class PredictionModelTest(TestCase):
    def test_prediction_creation(self):
        pred = Prediction.objects.create(
            sepal_length=5.1,
            sepal_width=3.5,
            petal_length=1.4,
            petal_width=0.2,
            predicted_class=0
        )
        self.assertEqual(pred.predicted_class, 0)
        
        
        