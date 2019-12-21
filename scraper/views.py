
# from django.shortcuts import render
from .models import PhysicsSite

from django.views.generic import ListView


class PhysicsView(ListView):
    # By using ListView you don't have to specify the template, '_list' is automatically added to the model name.
    paginate_by = 10
    model = PhysicsSite
