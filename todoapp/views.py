from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModels
from django.urls import reverse_lazy

# Create your views here.
class TodoList(ListView):
    template_name = "list.html"
    model = TodoModels

class TodoDetail(DetailView):
    template_name = "detail.html"
    model = TodoModels

class TodoCreate(CreateView):
    template_name = "create.html"
    model = TodoModels
    fields = ("title", "memo", "priority", "duedate")
    success_url = reverse_lazy("list")    # 成功したときにどのurlに飛ぶか reverse_lazy:viewからurlを指定する。list.htmlに飛ぶ

class TodoDelete(DeleteView):
    template_name = "delete.html"
    model = TodoModels
    success_url = reverse_lazy("list")

class TodoUpdate(UpdateView):
    template_name = "update.html"
    model = TodoModels
    fields = ("title", "memo", "priority", "duedate")
    success_url = reverse_lazy("list")