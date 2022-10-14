
from multiprocessing import context
from django import views
from django.shortcuts import render,redirect
from .forms import ReviewForm
from .models import Review




def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:create')
    else:
        review_form = ReviewForm()
    context = {
        'review_form' : review_form
    }
    return render(request,'reviews/create.html',context = context)

def index(request):
    reviews =  Review.objects.all()
    context={
        'reviews':reviews
    }
    return render(request, 'reviews/index.html',context)

def detail(request,pk):
    review = Review.objects.get(pk=pk)
    context ={
        'review':review
    }
    return render(request, 'reviews/detail.html',context)

def update(request,pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:detail',review.pk)
    else:
        review_form = ReviewForm(instance=review)
    context ={
        'review_form':review_form
    }
    return render(request, 'reviews/update.html',context)