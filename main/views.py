from django.shortcuts import render

from main.models import Student
from django.views.generic import ListView, DetailView


class StudentListViews(ListView):
    model = Student
    template_name = 'main/index.html'


class StudentDetailVIew(DetailView):
    model = Student
    template_name = 'main/student_detail.html'


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
