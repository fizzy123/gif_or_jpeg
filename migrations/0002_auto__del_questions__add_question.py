# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Questions'
        db.delete_table(u'gif_or_jpeg_questions')

        # Adding model 'Question'
        db.create_table(u'gif_or_jpeg_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('gif', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'gif_or_jpeg', ['Question'])


    def backwards(self, orm):
        # Adding model 'Questions'
        db.create_table(u'gif_or_jpeg_questions', (
            ('gif', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('photo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'gif_or_jpeg', ['Questions'])

        # Deleting model 'Question'
        db.delete_table(u'gif_or_jpeg_question')


    models = {
        u'gif_or_jpeg.question': {
            'Meta': {'object_name': 'Question'},
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