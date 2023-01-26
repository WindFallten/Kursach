import imp
from typing import Text
from .models import Articl, Comments
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class ArticlForm(ModelForm):
    class Meta:
        model = Articl
        fields = ['title' , 'info' , 'full_text' , 'data']

        widgets = {
            "title" : TextInput(attrs={
                'class': 'text-add' ,
                'placeholder' : 'Название вакансии' 
            }),
            "info" : TextInput(attrs={
                'class': 'text-add' ,
                'placeholder' : 'Зарплата' 
            }),
            "full_text" : Textarea(attrs={
                'class': 'text-add' ,
                'placeholder' : 'Полная информация по вакансии' 
            }),
            "data" : DateTimeInput(attrs={
                'class': 'text-add',
                'placeholder' : 'Дата публикации',
                'type' : 'date'
            })
        }

User = get_user_model()

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text',]

        widgets = {
            "text" : Textarea(attrs={
                'class': 'form__text' ,
                'placeholder' : 'Впишите отзыв'
            })
        }
