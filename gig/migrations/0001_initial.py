# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Gig'
        db.create_table('gig_gig', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hall', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal('gig', ['Gig'])


    def backwards(self, orm):
        
        # Deleting model 'Gig'
        db.delete_table('gig_gig')


    models = {
        'gig.gig': {
            'Meta': {'object_name': 'Gig'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'hall': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['gig']
