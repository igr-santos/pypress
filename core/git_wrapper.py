import os
import re
from django.conf import settings
from django.utils.text import slugify
from git import Repo


class GitWrapper(object):
    """

    """
    repo_path = settings.ENTRIES_REPO_FOLDER
    entries_branch = 'entries'
    workflow = [
        'core.git_wrapper.WriteToFile',
        'core.git_wrapper.AddFileToStage',
        'core.git_wrapper.SetGitConfig',
        'core.git_wrapper.CommitFile'
    ]

    def __init__(self):
        self.repo = Repo(self.get_repo_path())
        self.entries = self.repo.heads[self.entries_branch]

    def get_repo_path(self):
        return self.repo_path

    def commit(self, obj):
        self.pre_commit()
        self.execute_workflow(obj)
        self.post_commit()

    def pre_commit(self):
        self.entries.checkout()

    def post_commit(self):
        pass

    def execute_workflow(self, obj):
        res = {}
        workflow = self.get_workflow()

        for klass_name in workflow:
            klass = self.get_klass(klass_name)
            ret = klass.execute(self, obj, res)
            if not ret:
                break
            res[klass.__name__] = ret

        return res

    def get_workflow(self):
        return self.workflow

    def get_klass(self, name):
        module = '.'.join(name.split('.')[:-1])
        klass = name.split('.')[-1]
        m = __import__(module, fromlist=[klass])
        return getattr(m, klass)


class WriteToFile(object):
    filename_fld = 'title'
    content_fld = 'body'
    path = '_entries'

    @classmethod
    def execute(cls, gw, obj, res):
        filename = '{}.rst'.format(slugify(getattr(obj, cls.filename_fld)))
        full_path = os.path.join(gw.repo_path, cls.path, filename)
        with open(full_path, 'w+') as f:
            f.write(getattr(obj, cls.content_fld))
        return full_path


class AddFileToStage(object):
    """
    Could be many files to commit, but we want to have just one file
    in each commit, this class should get the file wrote by the
    WriteToFile class and commit it!
    """

    @classmethod
    def execute(cls, gw, obj, res):
        repo = gw.repo
        index = repo.index
        filename = cls.get_filename(res)

        files = repo.git.status('-z')
        if not files:
            return False

        files = files.split('\x00')
        file_to_commit, untracked = cls.parse_files(files, filename)
        if file_to_commit:
            index.add([file_to_commit])
            return {'untracked': untracked, 'filename': filename}
        return False

    @classmethod
    def get_filename(cls, res):
        try:
            return res.get('WriteToFile')
        except:
            return False

    @classmethod
    def parse_files(cls, files, filename):
        #pattern to find filename
        fn_patter = '^.+({})$'.format(filename.split('/')[-1])

        #pattern to find a file no matter if its untracked or not
        regex = ['^ M (.+)', '^\?{2} (.+)']

        for f in files:
            #we wanna add just the file with the given filename
            if not re.search(fn_patter, f):
                continue

            for i, p in enumerate(regex):
                m = re.search(p, f)
                if m:
                    return m.group(1), i


class SetGitConfig(object):

    @classmethod
    def execute(cls, gw, obj, res):
        config = gw.repo.config_writer()
        config.set_value("user", "email", obj.author.email)

        name = obj.author.get_full_name()
        if not name:
            name = obj.author.username
        config.set_value("user", "name", name)
        config.write()
        return config


class CommitFile(object):

    @classmethod
    def execute(cls, gw, obj, res):
        index = gw.repo.index
        author = obj.author

        try:
            untracked = res.get('AddFileToStage').get('untracked')
        except:
            untracked = False

        msg = '{};Author:{};Status:{}\n\n'.format(
            'Add' if untracked else 'Change',
            author.username,
            obj.status
        )
        index.commit(msg)
