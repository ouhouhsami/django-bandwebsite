# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        from django.db import connection, transaction
        cursor = connection.cursor()
        cursor.execute("UPDATE blog_post SET image = REPLACE(image, 'blog_image', 'dynamic/blog_image');")
        transaction.commit_unless_managed()
        cursor.execute("UPDATE multimedia_image SET image = REPLACE(image, 'media', 'dynamic/media');")
        transaction.commit_unless_managed()
        '''
        cursor.execute("UPDATE pro_article SET image = REPLACE(image, 'article_image', 'dynamic/article_image');")
        transaction.commit_unless_managed()
        cursor.execute("UPDATE pro_photospro SET image = REPLACE(image, 'pro_image', 'dynamic/pro_image');")
        transaction.commit_unless_managed()        
        cursor.execute("UPDATE pro_worksheetpdf SET pdf = REPLACE(pdf, 'worksheet', 'dynamic/worksheet');")
        transaction.commit_unless_managed()
        '''
        
    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
        'blog.artist': {
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Post']"}),
            'relateds': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Artist']", 'through': "orm['blog.ArtistPosition']", 'symmetrical': 'False'}),
            'x_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'y_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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
