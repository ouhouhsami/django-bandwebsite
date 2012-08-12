# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Slideshow'
        db.create_table('multimedia_slideshow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('multimedia', ['Slideshow'])

        # Adding model 'Image'
        db.create_table('multimedia_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('slideshow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Slideshow'])),
        ))
        db.send_create_signal('multimedia', ['Image'])

        # Adding model 'Video'
        db.create_table('multimedia_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('video', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slideshow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Slideshow'])),
        ))
        db.send_create_signal('multimedia', ['Video'])

        # Adding model 'Sound'
        db.create_table('multimedia_sound', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('sound', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slideshow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Slideshow'])),
        ))
        db.send_create_signal('multimedia', ['Sound'])


    def backwards(self, orm):
        
        # Deleting model 'Slideshow'
        db.delete_table('multimedia_slideshow')

        # Deleting model 'Image'
        db.delete_table('multimedia_image')

        # Deleting model 'Video'
        db.delete_table('multimedia_video')

        # Deleting model 'Sound'
        db.delete_table('multimedia_sound')


    models = {
        'multimedia.image': {
            'Meta': {'object_name': 'Image'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'slideshow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Slideshow']"}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.slideshow': {
            'Meta': {'object_name': 'Slideshow'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.sound': {
            'Meta': {'object_name': 'Sound'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slideshow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Slideshow']"}),
            'sound': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.video': {
            'Meta': {'object_name': 'Video'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slideshow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Slideshow']"}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['multimedia']
