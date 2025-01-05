from .models import Service, Team
from blog.models import Article
from django.views.generic import TemplateView, ListView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()[:3]
        context['teams'] = Team.objects.all()
        context['Articles'] = Article.objects.all()[:3]
        context['Articles'] = Article.objects.all()[:3]
        return context

class ServiceView(ListView):
    model = Service
    template_name = 'service.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutView(ListView):
    model = Team
    template_name = 'about.html'
