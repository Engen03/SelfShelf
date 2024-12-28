from django.urls import path
from .views import BookList, BookDetail, AuthorList, AuthorDetail

urlpatterns = [
    path('books/', BookList.as_view()),
    path('books/<int:pk>/', BookDetail.as_view()),
    path('authors/', AuthorList.as_view()),
    path('authors/<int:pk>/', AuthorDetail.as_view()),
]