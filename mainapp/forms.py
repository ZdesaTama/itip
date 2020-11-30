from django import forms
from .models import groups


class reg_stud(forms.Form):
    name = forms.CharField(help_text="Введите имя", label="Имя")
    fname = forms.CharField(help_text="Введите фомилию", label="Фамилия")
    arr = groups.objects.all()
    ch = []
    for i in range(len(arr)):
        ch.append((arr[i].name, arr[i].name))
    ch = tuple(ch)
    group = forms.ChoiceField(help_text="Выберите свою группу",
                              choices=ch, label="Группа")
    login = forms.CharField(help_text="Придумайте логин",
                            label="Логин", min_length=6)
    password = forms.CharField(
        help_text="Придумайте пароль", label="Пароль", min_length=6)


class loging(forms.Form):
    login = forms.CharField(help_text="Логин")
    password = forms.CharField(help_text="Пароль")
