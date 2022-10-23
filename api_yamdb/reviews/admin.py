from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User


@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'score', 'author', 'title')
    search_fields = ('title', 'author')
    list_filter = ('score', 'text',)
    empty_value_display = '-пусто-'


mymodels = [Category, Comment, Genre, Title, User]
admin.site.register(mymodels)
