from __future__ import unicode_literals

from django.db import models


class Quote(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price = models.CharField(max_length=18)

    def __str__(self):
        return ' '.join([
            self.name,
            self.type,
        ])

    def __init__(self, *args, **kwargs):
        super(Quote, self).__init__(*args, **kwargs)
