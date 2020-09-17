"""
Django views for trivia_app project.

Description:
index = for home page
question_one = for question one page
question_two = for question two page
summary= for summary page


"""
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'first/index.html')

def question_one(request):
    return render(request, 'first/q1.html')

def question_two(request):
    return render(request, 'first/q2.html')

def summary(request):
    return HttpResponse('<h1>summary</h1>')

def index_submission(request):
    print("submission succesfull")
    name=request.POST["name"]
    return redirect('question_one')

def question_one_submission(request):
    print("q submit success")
    return redirect('question_two')