from django.db import models


class Keyword(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(default="", blank=True)
    created_by = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(default="", blank=True)
    created_by = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=64)
    path = models.CharField(max_length=512, default="")
    link = models.CharField(max_length=512, default="")
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=0)
    keywords = models.ManyToManyField(Keyword, blank=True)
    created_by = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def all_tags(self):
        return ', '.join([x.name for x in self.keywords.all()])


class Monitor(models.Model):
    path = models.CharField(max_length=512, default="")
    last_checked = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
