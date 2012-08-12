from django.contrib import admin
from models import AlbumCategory, Album, AlbumArchive, Song, Track


class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'soundfile')
    list_editable = ('soundfile',)


admin.site.register(AlbumCategory)
admin.site.register(Album)
admin.site.register(Song, SongAdmin)
admin.site.register(Track)
admin.site.register(AlbumArchive)
