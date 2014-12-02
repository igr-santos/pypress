from django.db import models


class Config(models.Model):
    name = models.SlugField()
    value = models.TextField(blank=True)
    extra = models.TextField(blank=True)

    def __unicode__(self):
        return '{}={}'.format(self.name, self.value.__str__())
