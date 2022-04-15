#  Code taken form https://github.com/gomathishankar28/ms4_bubbles
from django.urls import path
from . import views

urlpatterns = [
    path("add_review/<product_id>", views.add_review, name="add_review"),
]
