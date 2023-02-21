from django.shortcuts import render
import joblib
import os
import json
import pandas as pd
from .models import Penguin_Prediction
import psycopg2


# Create your views here.

def index(request):
    return render(request,'index.html')

def result(request):
    model = joblib.load('../prediction_service/model/model.joblib')
    list = []
    list.append(float(request.GET['island']))
    list.append(float(request.GET['bill_length_mm']))
    list.append(float(request.GET['bill_depth_mm']))
    list.append(float(request.GET['flipper_length_mm']))
    list.append(float(request.GET['body_mass_g']))
    list.append(float(request.GET['sex']))
    answer = model.predict([list]).tolist()[0]

    b = Penguin_Prediction(island=request.GET['island'],bill_length_mm=request.GET['bill_length_mm'],bill_depth_mm=request.GET['bill_depth_mm'],flipper_length_mm=request.GET['flipper_length_mm'],body_mass_g=request.GET['body_mass_g'],sex=request.GET['sex'],species=answer)
    b.save()

    return render(request,"index.html",{'answer':answer})
