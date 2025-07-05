from django.http import JsonResponse
import joblib 
import numpy as np 
from .models import Prediction
from django.core.serializers import serialize
from django.http import HttpResponse

model = joblib.load('iris_model.pkl')

def home(request):
    return JsonResponse({'message': 'Welcome to Django Learning'})

def predict(request):
    sample = [0.2, 0.2, 2.0, 1.3]

    prediction = model.predict([sample])
    return JsonResponse({'prediction': int(prediction[0])})

# Saving the results 
def predict_result(request):
    try:
        a = float(request.GET.get('a'))
        b = float(request.GET.get('b'))
        c = float(request.GET.get('c'))
        d = float(request.GET.get('d'))
        sample = [a, b, c, d]
        prediction = model.predict([sample])[0]

        # Save to database
        Prediction.objects.create(
            sepal_length=a,
            sepal_width=b,
            petal_length=c,
            petal_width=d,
            predicted_class=int(prediction)
        )

        return JsonResponse({'prediction': int(prediction)})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    
# Django orm 
'''Now that your predictions are being saved in the database, let’s learn how 
to retrieve, filter, and manage that data using Django ORM (Object Relational Mapper).'''
def all_predictions(request):
    data = Prediction.objects.all().order_by('-timestamp')  # Latest first
    json_data = serialize('json', data)
    return HttpResponse(json_data, content_type='application/json')

