from django.shortcuts import render
from django.http.response import HttpResponse
import random


# Create your views here.
def index(req):
    lottos = []
    while len(lottos) < 6:
        lottos.append(random.randint(1,46))
        lottos = list(set(lottos))
    return HttpResponse(f"<h1>lottos번호 {lottos}</h1>")