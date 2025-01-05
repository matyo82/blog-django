from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from . import models
from .forms import CommentForm


class BlogListView(ListView):
    model = models.Article
    template_name = "blog/blog.html"


class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = models.Article.objects.exclude(id=self.object.id).order_by('-date')[:3]
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = models.Comment(
                article=self.object,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                comment=form.cleaned_data['comment'],
                status=False
            )
            comment.save()
        return self.render_to_response(self.get_context_data(form=form))
