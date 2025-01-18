from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


from .forms import ReviewForm
from .models import Review

# Create your views here.

# Class based View
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    
    # def get(self, request):
    #     form = ReviewForm()
    
    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

    
    # def post(self, request):
    #     form = ReviewForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
        
    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })


# def review(request):
#     if request.method == 'POST':
#         # existing_data = Review.objects.get(pk=1)
#         # form = ReviewForm(request.POST, instance=existing_data)
#         # form.save()
#         # Updating an instance in databse is possible by using ModelForm as shown above. 
#         # IT'S JUST A DEMONSTRATION, NOT VALID WITH GIVEN DATA IN THAT EXAPMLE
        
#         form = ReviewForm(request.POST)
        
#         if form.is_valid():
#             # review = Review(
#             #     user_name=form.cleaned_data['user_name'], 
#             #     review_text=form.cleaned_data['review_text'], 
#             #     rating=form.cleaned_data['rating'])
#             # review.save()
#             # the code below does the same as the code above if it's ModelForm. It saves form/data in database
#             form.save()
#             return HttpResponseRedirect("/thank-you")
        
#     else:
#         form = ReviewForm()
    
#     return render(request, "reviews/review.html", {
#         "form": form
#     })


class ThankYouView(TemplateView):
    template_name = "reviews/thank-you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    
# def thank_you(request):
#     return render(request, "reviews/thank-you.html")


class ReviewsListView(ListView):
    template_name = "reviews/review-list.html"
    model = Review
    context_object_name = "reviews"
    # "object_list" for default
    
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=2)
    #     return data
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context

    
class SingleReviewView(DetailView):
    template_name = "reviews/single-review.html"
    model = Review
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context
    
    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # review_id = kwargs["id"]
        # selected_review = Review.objects.get(id=review_id)
        # context["review"] = selected_review
        # return context
        

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)