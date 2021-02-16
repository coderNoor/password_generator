from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def newhome(request):
    #return HttpResponse("Welcome To New Password Generator app!!")
    return render(request,'new_generator/newhome.html')

def newpassword(request):
    newCharacters = list('abcdefghijklmnopqrstuvwxyz')
    newpasswords = ''
    length = int(request.GET.get('length'))
    passwordUser = request.GET.get('passwordbyuser')
    if request.GET.get('UpperCase'):
        newCharacters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        newCharacters.extend(list('0123456789'))
    if request.GET.get('SpecialCharacters'):
        newCharacters.extend(list('@#$!%^&*'))

    for x in range(length):
        newpasswords += random.choice(newCharacters)
    return render(request,"new_generator/newpassword.html",{'newpassword':newpasswords,'UserPassword':passwordUser})
