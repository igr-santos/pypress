from django.db import models, OperationalError
from django.core.urlresolvers import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from .tags import TaggedWhatever


ENTRY_DRAFT = 'D'
ENTRY_PUBLISHED = 'P'
ENTRY_APPROVED = 'A'
ENTRY_STATUS_CHOICES = (
    (ENTRY_DRAFT, 'Draft'),
    (ENTRY_PUBLISHED, 'Published'),
    (ENTRY_APPROVED, 'Approved')
)


class EntryQueryset(models.QuerySet):

    def published(self):
        return self.filter(status=ENTRY_APPROVED).order_by('-published_at')


class Entry(models.Model):
    author = models.ForeignKey('auth.User', editable=False)
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=165, unique=True)
    body = models.TextField()
    tags = TaggableManager(through=TaggedWhatever)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    published_at = models.DateTimeField(editable=False, null=True, blank=True)
    status = models.CharField(max_length=1, default=ENTRY_DRAFT,
                              choices=ENTRY_STATUS_CHOICES, editable=False)

    objects = EntryQueryset.as_manager()

    class Meta:
        verbose_name_plural = 'Entries'
        ordering = ['-created_at', '-published_at']

    def __unicode__(self):
        return self.title

    def publish(self):
        if not self.published_at:
            self.status = ENTRY_PUBLISHED
            self.published_at = timezone.now()
            self.save()
            return self
        raise OperationalError('Entry published, not possible publish now.')

    def accept(self):
        if self.published_at and self.status == ENTRY_PUBLISHED:
            self.status = ENTRY_APPROVED
            self.save()
            return self
        raise OperationalError('Entry can\'t accept, entry not published.')

    def get_absolute_url(self):
        return reverse('blog:list-entry')
