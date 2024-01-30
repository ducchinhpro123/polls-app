from django.urls import path

from polls import views


app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # /polls/1
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # /polls/1/results
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # /polls/1/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
