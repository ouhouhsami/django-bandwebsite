from django.contrib import admin
from models import Category, Post, Artist


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    list_editable = ('image',)
    model = Artist


class PostAdmin(admin.ModelAdmin):
    model = Post

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Artist, ArtistAdmin)
