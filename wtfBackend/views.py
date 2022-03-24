from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from .models import *
from PIL.Image import new
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, FormView, TemplateView, DetailView, ListView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AdminPasswordChangeForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.edit import FormMixin
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import datetime
import base64
import json 
import random
import base64
from io import BytesIO
import csv, io
import json
# Create your views here.
#Homepage Landing Page
def Homepage(request):

    return render(request, "index.html")

def WtfWordAPI(request, word):
    new_word = WtfWord.objects.filter(name=word).first()
    if new_word is None:
        new_word = WtfWord.objects.all().order_by('?').first()
    context = {'word': new_word.name, "definition": new_word.definition}   
    return JsonResponse(context)


#this is second step when the actual csv is uploaded 
def AddWords(request):
    path3 = 'wtfBackend/files/web3_words.csv'
    with open(path3) as f:
        for line in f:
            line = line.split(',') 
            word = line[0]
            definition = line[1]
            new_word = WtfWord.objects.get_or_create(name=word, definition=definition)

    return HttpResponse("Success")