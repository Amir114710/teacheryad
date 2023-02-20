from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from teacher.models import Teacher


class ListDetailView(ListView):
    model = Teacher
    paginate_by = 6
    ordering = ('-is_teacher',)
    queryset = Teacher.objects.filter(is_teacher=True)
    template_name = 'post/list_detail.html'


class DetailView(DetailView):
    model = Teacher
    template_name = 'post/detail.html'


def SearchListView(request):
    q = request.GET.get('q')
    teacher = Teacher.objects.filter(name_field__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(teacher, 3)
    object_list = paginator.get_page(page_number)
    return render(request, 'post/list_detail.html', {"object_list": object_list, "page_obj": object_list})
