from django.db import OperationalError
from django.test import TestCase
from model_mommy import mommy


class EntryModelTest(TestCase):

    def setUp(self):
        self.entry = mommy.make('core.Entry')

    def test_unicode(self):
        """
        should return unicode method 'title'
        """
        self.assertEqual(self.entry.title, self.entry.__unicode__())

    def test_publish_entry(self):
        """
        should publish on call method
        """
        published_at = self.entry.publish()
        self.assertIsNotNone(published_at)

    def test_publish_entry_unique_error(self):
        """
        should return error if publish 2x
        """
        with self.assertRaises(OperationalError):
            self.entry.publish()
            self.entry.publish()

    def test_save_tags(self):
        """
        should save tags in entry
        """
        tagged = ['python', 'groups', 'language']
        self.entry.tags = tagged
        self.entry.save()
        self.assertEqual(self.entry.tags, tagged)
