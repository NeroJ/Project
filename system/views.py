from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from models import Student
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def Home(request):
    return render_to_response('home.html')
 
def Score(request):
    p=Student.objects.filter(StudentID=request.user)
    return render_to_response('score.html',{'p': p})
    
def Room1(request):
    p=Student.objects.filter(StudentID=request.user)
    return render_to_response('room1.html',{'p': p})

def Management(request):
    p=Student.objects.filter(StudentID=request.user)
    return render_to_response('management.html',{'p': p})

def Arbitrary(request): 
    p=Student.objects.filter(StudentID=request.user)
    return render_to_response('arbitrary.html',{'p': p})

def Socialism(request):
    p=Student.objects.filter(StudentID=request.user)
    return render_to_response('socialism.html',{'p': p})

def Compulsory(request):
    p=Student.objects.filter(StudentID=request.user)
    return render_to_response('compulsory.html',{'p': p})

def Result(request):
    p=Student.objects.filter(StudentID=request.user)
    return render_to_response('result.html',{'p': p})

def Timetable(request): 
    p=Student.objects.filter(StudentID=request.user)
    return render_to_response('timetable.html',{'p': p})