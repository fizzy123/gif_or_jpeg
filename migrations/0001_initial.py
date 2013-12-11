# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Session'
        db.create_table(u'gif_or_jpeg_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('questions', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
        ))
        db.send_create_signal(u'gif_or_jpeg', ['Session'])

        # Adding model 'Questions'
        db.create_table(u'gif_or_jpeg_questions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('gif', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'gif_or_jpeg', ['Questions'])


    def backwards(self, orm):
        # Deleting model 'Session'
        db.delete_table(u'gif_or_jpeg_session')

        # Deleting model 'Questions'
        db.delete_table(u'gif_or_jpeg_questions')


    models = {
        u'gif_or_jpeg.questions': {
            'Meta': {'object_name': 'Questions'},
            'correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'gif_or_jpeg.session': {
            'Meta': {'object_name': 'Session'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questions': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['gif_or_jpeg']