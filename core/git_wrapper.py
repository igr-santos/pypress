from django.conf import settings
from git import Repo


class GitWrapper(object):
    branch_name = 'entries'

    def __init__(self):
        self.repo = Repo(settings.BASE_DIR)
        self.entries = self.repo.heads[self.branch_name]

    def commit(self, filename):
        rp = self.repo
        #rp.heads.entries.checkout()
        import pdb; pdb.set_trace()
