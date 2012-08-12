# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AlbumCategory'
        db.create_table('music_albumcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('music', ['AlbumCategory'])

        # Adding model 'Album'
        db.create_table('music_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('cover', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('album_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.AlbumCategory'])),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('music', ['Album'])

        # Adding model 'Song'
        db.create_table('music_song', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('soundfile', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Album'], blank=True)),
            ('track_number', self.gf('django.db.models.fields.IntegerField')()),
            ('text', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('lyrics', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('tab', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('music', ['Song'])

        # Adding model 'Track'
        db.create_table('music_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Song'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('instrument', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('music', ['Track'])


    def backwards(self, orm):
        
        # Deleting model 'AlbumCategory'
        db.delete_table('music_albumcategory')

        # Deleting model 'Album'
        db.delete_table('music_album')

        # Deleting model 'Song'
        db.delete_table('music_song')

        # Deleting model 'Track'
        db.delete_table('music_track')


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
