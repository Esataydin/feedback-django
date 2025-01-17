from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ReviewForm
from .models import Review

# Create your views here.

# Class based View
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
    
        return render(request, "reviews/review.html", {
            "form": form
        })

    
    def post(self, request):
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "reviews/review.html", {
            "form": form
        })


def review(request):
    if request.method == 'POST':
        # existing_data = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance=existing_data)
        # form.save()
        # Updating an instance in databse is possible by using ModelForm as shown above. 
        # IT'S JUST A DEMONSTRATION, NOT VALID WITH GIVEN DATA IN THAT EXAPMLE
        
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            # review = Review(
            #     user_name=form.cleaned_data['user_name'], 
            #     review_text=form.cleaned_data['review_text'], 
            #     rating=form.cleaned_data['rating'])
            # review.save()
            # the code below does the same as the code above if it's ModelForm. It saves form/data in database
            form.save()
            return HttpResponseRedirect("/thank-you")
        
    else:
        form = ReviewForm()
    
    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank-you.html")