# core/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Skill, Experience, Project, Education, BlogPost
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = Project.objects.filter(featured=True)[:3]
        context['skills'] = Skill.objects.all()[:6]
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['education'] = Education.objects.all()
        return context


class SkillsView(ListView):
    model = Skill
    template_name = 'skills.html'
    context_object_name = 'skills'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skill_categories'] = Skill.CATEGORY_CHOICES
        return context


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['technologies'] = Skill.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail.html'
    context_object_name = 'project'
    slug_url_kwarg = 'project_slug'


class ExperienceView(ListView):
    model = Experience
    template_name = 'experience.html'
    context_object_name = 'experiences'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your message has been sent. Thank you!')
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = 'contact_success.html'


from django.views.generic import ListView
from .models import BlogPost

# core/views.py
from django.views.generic import ListView
from .models import BlogPost

# core/views.py
from django.views.generic import ListView
from .models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'  # Adjust this if needed
    context_object_name = 'blog_posts'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


