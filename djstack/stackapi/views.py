from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question
from .serializer import QuestionSerializer
from bs4 import BeautifulSoup

import requests
import json

# Create your views here.


def index(request):
    return HttpResponse("Success")


class QuestionAPI(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


def latest(request):
    try:
        res = requests.get("https://stackoverflow.com/questions")

        soup = BeautifulSoup(res.text, "html.parser")

        questions = soup.select(".question-summary")
        for que in questions:
            #Preluam intrebarea
            q = que.select_one('.question-hyperlink').getText()
            #Preluam numarul de voturi
            vote_count = que.select_one('.vote-count-post').getText()
            #Preluam numarul de vizualizari
            views = que.select_one('.views').attrs['title']
            #Preluam tagurile intrebariilor
            
            tags = [i.getText() for i in (que.select('.post-tag'))]
            #Inregistram un obiect de tipul Question 
            question = Question()
            
            #Ingregistram in obiectul Question.vote_count
            #  numarul de voturi preluate mai sus in variabila vote_count
            question.question = q

            #Ingregistram in obiectul Question.vote_count
            #  numarul de voturi preluate mai sus in variabila vote_count
            question.vote_count = vote_count
            
            #Ingregistram in obiectul Question.views 
            #  numarul de vizualizari preluate mai sus in variabila views
            question.views = views

            #Ingregistram in obiectul Question.tags
            #  numarul de vizualizari preluate mai sus in variabila tags
            question.tags = tags
            #Salvam in baza de date intrebarea cu datele preluate mai sus
            question.save()
        return HttpResponse("Latest Data Fetched from Stack Overflow")
    except e as Exception:
        return HttpResponse(f"Failed {e}")
