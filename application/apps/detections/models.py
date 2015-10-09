import datetime

from flask.helpers import url_for
from mongoengine import fields

from application.apps.base.models import BaseDocument
from application.apps.person.models import MissedPerson


class Detection(BaseDocument):
    received_at = fields.DateTimeField(default=datetime.datetime.now(), required=True)
    face = fields.ImageField(required=True)
    time = fields.DateTimeField(required=True)
    person = fields.ReferenceField(MissedPerson, required=True)
    # location = fields.ReferenceField(Detector)

    def get_absolute_url(self):
        return url_for('detection', kwargs={'detection_id': self.id})

    def __unicode__(self):
        return "Detection {}".format(self.received_at)

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
    }
