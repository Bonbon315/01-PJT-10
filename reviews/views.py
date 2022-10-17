from multiprocessing import context
from django import views
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required


def index(request):
    reviews = Review.objects.all()
    context = {"reviews": reviews}
    return render(request, "reviews/index.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {"review": review}
    return render(request, "reviews/detail.html", context)


@login_required
def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
    context = {"review_form": review_form}
    return render(request, "reviews/create.html", context=context)


@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:detail", review.pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {"review_form": review_form}
    return render(request, "reviews/update.html", context)


@login_required
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect("reviews:index")
    return render(request, "reviews/detail.html")
