from django.db import models, OperationalError
from django.utils import timezone
from taggit.managers import TaggableManager
from .tags import TaggedWhatever


class Entry(models.Model):
    author = models.ForeignKey('auth.User', editable=False)
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
