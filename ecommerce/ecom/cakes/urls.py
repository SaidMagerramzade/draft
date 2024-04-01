from django.urls import path
from . import views


app_name = "cakes"

urlpatterns = [
    path(
        "", 
        views.IndexView.as_view(), 
        name="home"
        ),
    path(
        "desertler/<int:pk>-<slug:slug>/", 
        views.cake_detail_view, 
        name="details"
        ),
    path(
        "about/", 
        views.AboutView.as_view(), 
        name="about"
        ),
    path(
        "contacts/", 
        views.ContactsView.as_view(), 
        name="contacts"
        ),
    path(
        "send-mail/",
        views.SendMailView.as_view(),
        name="send-mail"
    ),
    path(
        "json/",
        views.json.as_view(),
        name="json"
    ),
    path(
        "latest/",
        views.LatestCakeView.as_view(),
        name="latest"
    ),
    path(
        "new-cake/",
        views.CreateCakeView.as_view(),
        name="create-cake"
    ),
    path(
        "success/",
        views.success_view,
        name="success"
    ),
    path(
        "login/",
        views.LoginView.as_view(),
        name="login"
    ),
    path(
        'delete/<int:pk>/',
        views.CakeDeleteView.as_view(),
        name='cake-delete'
    ),
    path(
        "rating/",
        views.CakeRatingView.as_view(),
        name='rating'
    )
]