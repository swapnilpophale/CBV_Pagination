from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

class ArticleView(ListView):
    model = Article
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 1

