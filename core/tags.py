from django.db import models
from taggit.models import TagBase, GenericTaggedItemBase


class TagEntry(TagBase):

    class Meta:
        verbose_name = 'Tag Entry'
        verbose_name_plural = 'Tags Entry'


class TaggedWhatever(GenericTaggedItemBase):
    tag = models.ForeignKey(TagEntry,
                            related_name="%(app_label)s_%(class)s_tags")
