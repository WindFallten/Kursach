from distutils.log import error
from importlib.resources import path
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Articl, Category
from .forms import ArticlForm, CommentForm
from django.views import View
from django.contrib.auth import authenticate , login
from main.forms import UserCreationForm
from django.views.generic import DetailView , UpdateView , DeleteView
from django.views.generic.edit import FormMixin
from django.core.paginator import Paginator
from django_filters.rest_framework import DjangoFilterBackend

class register(View):

    template_name = 'registration/register.html'

    def get(self,request):
        context = {
            'form' : UserCreationForm()
        }
        return render(request, self.template_name , context)
    
    def post(self , request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            return redirect('login')
        context = {
            'form' : form
        }
        return render(request, self.template_name , context)

class VacanseDetailView(DetailView, FormMixin):
    model = Articl
    template_name = 'main/vacansePodrobno.html'
    context_object_name = 'articles'
    form_class = CommentForm
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('vacase-detail', kwargs = {'pk':self.get_object().id})

    def post(self, request, *arhs, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else: 
            return self.form_invalid(form)
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.article = self.get_object()
        self.object.save()
        return super().form_valid(form)

            

class VacanseUpdateView(UpdateView):
    model = Articl
    template_name = 'main/addform.html'

    form_class = ArticlForm

class VacanseDeleteView(DeleteView):
    model = Articl
    success_url = '/vacanse/'
    template_name = 'main/delete.html'

def index(request): 
    data = {
        'title' : 'Главная страница ',
        'values': ['some' , 'people' , 'hello'],
        'obj': {
            'date': '18.03',
            'age': '18',
            'car': 'bmw'
        }
    }
    return render(request , 'main/index.html' , data)


def vacanse(request):
    category = Category.objects.all()
    vacanses = Articl.objects.all()
    paginator = Paginator(vacanses, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    search_query = request.GET.get('search' , '')
    if search_query:
        page_obj = Articl.objects.filter(title__icontains = search_query)
    else:
        vacanses = Articl.objects.all()
    return render(request , 'main/vacanse.html' , {'page_obj': page_obj, 'category': category})

def vacanse__category(request, url):
    category = Category.objects.all()
    vacanses = Articl.objects.filter(cat = url)
    paginator = Paginator(vacanses, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # search_query = request.GET.get('search' , '')
    # if search_query:
    #     page_obj = Articl.objects.filter(title__icontains = search_query)
    # else:
    #     vacanses = Articl.objects.all()
    return render(request , 'main/vacanse.html' , {'page_obj': page_obj, 'category': category})

def vacansePodrobno(request):
    vacanses = Articl.objects.all()
    
    return render(request , 'main/vacansePodrobno.html' , {'vacanses': vacanses})

def rabotadatel(request):
    return render(request , 'main/rabotadatel.html')

def vacanseRabotadatel(request):
    vacanses = Articl.objects.all()
    return render(request , 'main/vacanseRabotadatel.html' , {'vacanses': vacanses})

def addform(request):
    error = ''
    if request.method == 'POST':
        form = ArticlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacanse')
        else:
            error = 'Форма заполнена не верно'

    form = ArticlForm()

    data = {
        'form' : form,
        'error' : error
    }

    return render(request , 'main/addform.html' , data )