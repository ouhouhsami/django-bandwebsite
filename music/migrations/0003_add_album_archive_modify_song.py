# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AlbumArchive'
        db.create_table('music_albumarchive', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Album'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('archive', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('music', ['AlbumArchive'])

        # Changing field 'Song.soundfile'
        db.alter_column('music_song', 'soundfile', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True))


    def backwards(self, orm):
        
        # Deleting model 'AlbumArchive'
        db.delete_table('music_albumarchive')

        # Changing field 'Song.soundfile'
        db.alter_column('music_song', 'soundfile', self.gf('django.db.models.fields.URLField')(max_length=200))


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
        'music.albumarchive': {
            'Meta': {'object_name': 'AlbumArchive'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Album']"}),
            'archive': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'soundfile': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
