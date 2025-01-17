from django.urls import path

from . import views

urlpatterns = [
    # path("", views.review), # Method based view
    path("", views.ReviewView.as_view()), # Class based view
    path("thank-you", views.thank_you)
]
