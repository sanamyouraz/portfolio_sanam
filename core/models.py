# core/models.py
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('LANGUAGE', 'Programming Language'),
        ('FRAMEWORK', 'Framework/Library'),
        ('DATABASE', 'Database'),
        ('TOOL', 'Tool/Platform'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon = models.FileField(upload_to='skills/', blank=True, null=True)
    proficiency = models.IntegerField(default=80, help_text="Proficiency level from 0-100")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['category', '-proficiency']


class Experience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = RichTextField()
    company_logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return f"{self.position} at {self.company}"

    class Meta:
        ordering = ['-start_date']


class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=255)
    description = RichTextField()
    technologies = models.ManyToManyField(Skill)
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    completion_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-completion_date']


class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = "Education"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField  # assuming you are using CKEditor

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextField()
    featured_image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    tags = models.CharField(max_length=255, help_text="Comma separated tags")
    is_featured = models.BooleanField(default=False)  # Add this line for the featured post

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def split_tags(self):
        """Returns list of tags split from the tags field"""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []

    class Meta:
        ordering = ['-created_at']

    class Meta:
        ordering = ['-created_at']


