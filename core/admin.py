from django.contrib import admin
from .models import Skill, Experience, Project, Education, Contact, BlogPost

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'current')
    list_filter = ('current', 'start_date')
    search_fields = ('company', 'position')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'completion_date')
    list_filter = ('featured', 'completion_date')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date', 'current')
    list_filter = ('current', 'start_date')
    search_fields = ('institution', 'degree')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'read')
    list_filter = ('read', 'created_at')
    search_fields = ('name', 'email', 'subject')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at', 'updated_at')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'tags')
    prepopulated_fields = {'slug': ('title',)}
