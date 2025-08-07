from django.shortcuts import render, redirect
from django.db.models import Count
from django.http import JsonResponse

import json
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


def submit_todo(request):
    if request.method == "POST":
        data = json.loads(request.body)

        first_name = data.get("first_name", "").strip()
        items = data.get("items", [])

        # Consider a profanity filter

        todo = ToDoList.objects.create(
            first_name=first_name,
            # items=clean_items  --Profanity filter
            ip_address=get_client_ip(request)
        )

        return JsonResponse({"message": "List submitted!", "id": todo.id})
    
    return JsonResponse({"error": "POST only"}, status=405)


def get_client_ip(request):
    # Handles reverse proxy setups
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def random_todo_list(request):
    count = ToDoList.objects.filter(is_flagged=False).count()
    if count == 0:
        return JsonResponse({"error": "No lists available."}, status=404)
    random_index = random.randint(0, count - 1)
    todo = ToDoList.objects.filter(is_flagged=False)[random_index]
    return JsonResponse({"items": todo.items})
