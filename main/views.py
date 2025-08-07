from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse
import random

from .models import ToDoList


def home(request):
    return render(request, "main/index.html")


def cliches(request):
    return render(request, "main/cliche.html")


def blog(request):
    return render(request, "main/blog.html")


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")


def random_todo_list(request):
    count = ToDoList.objects.filter(is_flagged=False).count()
    if count == 0:
        return JsonResponse({"error": "No lists available."}, status=404)
    random_index = random.randint(0, count - 1)
    todo = ToDoList.objects.filter(is_flagged=False)[random_index]
    return JsonResponse({"items": todo.items})
