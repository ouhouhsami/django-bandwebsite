# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('blog_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('blog', ['Category'])

        # Adding model 'Post'
        db.create_table('blog_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Category'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('text', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal('blog', ['Post'])

        # Adding model 'Artist'
        db.create_table('blog_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('x_position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('y_position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('blog', ['Artist'])

        # Adding M2M table for field posts on 'Artist'
        db.create_table('blog_artist_posts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artist', models.ForeignKey(orm['blog.artist'], null=False)),
            ('post', models.ForeignKey(orm['blog.post'], null=False))
        ))
        db.create_unique('blog_artist_posts', ['artist_id', 'post_id'])

        # Adding model 'ArtistPosition'
        db.create_table('blog_artistposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subject', to=orm['blog.Artist'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(related_name='target', to=orm['blog.Artist'])),
            ('proximity_factor', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('blog', ['ArtistPosition'])

        # Adding unique constraint on 'ArtistPosition', fields ['artist', 'related']
        db.create_unique('blog_artistposition', ['artist_id', 'related_id'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('blog_category')

        # Deleting model 'Post'
        db.delete_table('blog_post')

        # Deleting model 'Artist'
        db.delete_table('blog_artist')

        # Removing M2M table for field posts on 'Artist'
        db.delete_table('blog_artist_posts')

        # Deleting model 'ArtistPosition'
        db.delete_table('blog_artistposition')

        # Removing unique constraint on 'ArtistPosition', fields ['artist', 'related']
        db.delete_unique('blog_artistposition', ['artist_id', 'related_id'])


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
