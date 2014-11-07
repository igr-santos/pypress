from django.db import models, OperationalError
from django.utils import timezone
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


class TagEntry(TagBase):

    class Meta:
        verbose_name = 'Tag Entry'
        verbose_name_plural = 'Tags Entry'


class TaggedWhatever(GenericTaggedItemBase):
    tag = models.ForeignKey(TagEntry,
                            related_name="%(app_label)s_%(class)s_tags")


class Entry(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=165)
    body = models.TextField()
    tags = TaggableManager(through=TaggedWhatever)
    draft = models.BooleanField(default=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    published_at = models.DateTimeField(editable=False, null=True, blank=True)

    class Meta:
        ordering = ['-created_at', '-published_at']

    def __unicode__(self):
        return self.title

    def publish(self):
        if not self.published_at:
            self.draft = False
            self.published_at = timezone.now()
            self.save()
            return self.published_at
        raise OperationalError('Entry published, not possible publish now.')
