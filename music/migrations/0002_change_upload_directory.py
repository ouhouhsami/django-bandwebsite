# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from music.models import *

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        from django.db import connection, transaction
        cursor = connection.cursor()
        cursor.execute("UPDATE music_album SET cover = REPLACE(cover, 'media', 'dynamic/media');")
        transaction.commit_unless_managed()
        cursor.execute("UPDATE music_song SET tab = REPLACE(tab, 'media', 'dynamic/media');")
        transaction.commit_unless_managed()

    def backwards(self, orm):
        from django.db import connection, transaction
        cursor = connection.cursor()
        cursor.execute("UPDATE music_album SET cover = REPLACE(cover, 'dynamic/media', 'media');")
        transaction.commit_unless_managed()
        cursor.execute("UPDATE music_song SET tab = REPLACE(tab, 'dynamic/media', 'media');")
        transaction.commit_unless_managed()

    models = {
        'music.album': {
            'Meta': {'object_name': 'Album'},
            'album_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.AlbumCategory']"}),
            'cover': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'music.albumcategory': {
            'Meta': {'object_name': 'AlbumCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        'music.song': {
            'Meta': {'object_name': 'Song'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Album']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lyrics': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'soundfile': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'tab': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'track_number': ('django.db.models.fields.IntegerField', [], {})
        },
        'music.track': {
            'Meta': {'object_name': 'Track'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrument': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Song']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['music']
