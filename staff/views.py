from django.shortcuts import render
from .form import CreateUserForm
from .models import Staff
from django.views.generic import CreateView


class StaffCreate(CreateView):
    template_name = "staff/create.html"
    model = Staff
    fields = ("id", "name", "password", "roll", "nyushabi", "taishabi", "hyoujijyun", "jikyu", "delete")
    ##success_url = reverse_lazy("list")