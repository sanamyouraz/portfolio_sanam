# core/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Skill, Experience, Project, Education, BlogPost
from .forms import ContactForm

from django.views.generic import TemplateView
from .models import Project, Skill, Resume  # Import Resume model

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = Project.objects.filter(featured=True)[:3]
        context['skills'] = Skill.objects.all()[:6]
        context['resume'] = Resume.objects.last()  # Get latest uploaded resume
        return context



class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['education'] = Education.objects.all()
        context['resume'] = Resume.objects.last()  # Get latest uploaded resume
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming 'related_projects' is a queryset of other projects related to the current project
        context['related_projects'] = Project.objects.exclude(slug=self.kwargs['project_slug'])[
                                      :4]  # Example: exclude the current project and get the first 4 related projects

        return context


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


# core/views.py
from django.views.generic import ListView
from django.db.models import Q
from .models import BlogPost

# views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPost

from django.views.generic import ListView
from .models import BlogPost
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'  # Make sure this matches your template location
    context_object_name = 'posts'  # Match the variable name in template
    paginate_by = 9  # Add pagination as shown in template

from django.views.generic import DetailView
from django.db.models import Q
from .models import BlogPost

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_post = self.get_object()

        # Get tags from current post
        current_tags = current_post.split_tags

        if current_tags:
            # Build a Q object to filter by tags
            tag_filter = Q()
            for tag in current_tags:
                tag_filter |= Q(tags__icontains=tag)

            related_posts = BlogPost.objects.filter(tag_filter).exclude(id=current_post.id).distinct()[:3]
        else:
            related_posts = BlogPost.objects.exclude(id=current_post.id)[:3]  # fallback

        context['related_posts'] = related_posts
        return context


