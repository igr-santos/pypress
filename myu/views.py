from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .forms import MyUserCreationForm


class UserListView(ListView):
    queryset = User.objects.all()
    paginate_by = 10


class UserCreateView(CreateView):
    model = User
    form_class = MyUserCreationForm
    success_url = reverse_lazy('adm:user-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UserEditView(UpdateView):
    model = User
    success_url = reverse_lazy('adm:user-list')
