from django.urls import path

from . import views

urlpatterns = [
    # path("", views.review), # Method based view
    path("", views.ReviewView.as_view()), # Class based view
    path("thank-you", views.ThankYouView.as_view()),
    # path("thank-you", views.thank_you),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view())
]
