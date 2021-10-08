from django.shortcuts import render
from cbvapp.models import Employees
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class EmployeeListView(ListView):
    model = Employees

class EmployeeDetailView(DetailView):
    model = Employees

class EmployeeCreateView(CreateView):
    model= Employees
    fields= ('ename','empid','esal','eaddr')

class EmployeeUpdateView(UpdateView):
    model=Employees
    fields = ('esal','eaddr')

class EmployeeDeleteView(DeleteView):
    model=Employees
    success_url = reverse_lazy('home')