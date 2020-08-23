from django.shortcuts import render
from django.views import generic
from .models import Note
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

# Create your views here.


class HomePageListView(LoginRequiredMixin, generic.ListView):
    model = Note


class NoteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Note
    fields = ('title', 'note', 'related_tag')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note


class NoteEditView(LoginRequiredMixin, generic.UpdateView):
    model = Note
    fields = ('title', 'note', 'related_tag')
    template_name = 'app/note_update.html'


class NoteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Note
    success_url = reverse_lazy('app:all-notes')


def note_search(request):
    query = request.GET.get('q')
    queryset = Note.objects.all()

    if query:
        queryset = queryset.filter(related_tag__icontains=query)

    return render(request, 'app/note_search.html', {'results': queryset})
