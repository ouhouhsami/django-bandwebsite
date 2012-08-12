# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'Artist', fields ['name']
        db.create_unique('blog_artist', ['name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Artist', fields ['name']
        db.delete_unique('blog_artist', ['name'])


    models = {
        'blog.artist': {
            'Meta': {'object_name': 'Artist'},
            'birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'death': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'genres': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.MusicGenre']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Post']"}),
            'relateds': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Artist']", 'through': "orm['blog.ArtistPosition']", 'symmetrical': 'False'})
        },
        'blog.artistposition': {
            'Meta': {'unique_together': "(('artist', 'related'),)", 'object_name': 'ArtistPosition'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subject'", 'to': "orm['blog.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proximity_factor': ('django.db.models.fields.IntegerField', [], {}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'target'", 'to': "orm['blog.Artist']"})
        },
        'blog.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'blog.musicgenre': {
            'Meta': {'object_name': 'MusicGenre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.MusicGenre']", 'null': 'True', 'blank': 'True'})
        },
        'blog.post': {
            'Meta': {'object_name': 'Post'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']
