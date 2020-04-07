# Django
from django.urls import path

# Views
from posts import views


urlpatterns = [
    path(
        route='',
        view=views.PostListView.as_view(),
        name='feed'
    ),
    path(
        route='posts/new/',
        view=views.create_post,
        name='create'
    ),
]
