from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from teacher.models import Teacher
from .models import Like
from django.http import JsonResponse


class ListDetailView(ListView):
    model = Teacher
    paginate_by = 6
    ordering = ('-is_teacher',)
    queryset = Teacher.objects.filter(is_teacher=True)
    template_name = 'post/list_detail.html'


class DetailView(DetailView):
    model = Teacher
    template_name = 'post/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.likes.filter(teacher__username = self.object.username , user_id = self.request.user.id).exists():
            context['is_like'] = True
        else:
            context['is_like'] = False
        return context


def SearchListView(request):
    q = request.GET.get('q')
    teacher = Teacher.objects.filter(name_field__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(teacher, 3)
    object_list = paginator.get_page(page_number)
    return render(request, 'post/list_detail.html', {"object_list": object_list, "page_obj": object_list})


def like(request , id , pk):
    try:
        like = Like.objects.get(teacher__id = id  , user_id=request.user.id)
        like.delete()
    except:
        Like.objects.create(teacher_id=pk , user_id = request.user.id)
    return redirect('post:user_Detail' , pk)
