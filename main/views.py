from django.shortcuts import render

from main.models import Student
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy


class StudentListViews(ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contact.html', context)


class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('main:index')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('main:index')
