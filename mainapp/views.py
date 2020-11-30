from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import users, list_items, works
from .forms import reg_stud, loging


def index(request):
    if request.session.has_key('user'):
        login = request.session['user']
        user = users.objects.filter(login=login)
        if user[0].group == 'teacher':
            name = user[0].FCs
            work = works.objects.filter(FCs=str(name))
            list_groups = []
            for i in work:
                if len(list_groups) != 0:
                    for k in list_groups:
                        if k != [i.group, i.nmae_item]:
                            list_groups.append([i.group, i.nmae_item])
                else:
                    list_groups.append([i.group, i.nmae_item])
            return render(request, 'index.html', context={"list_groups": list_groups})
        else:
            group = user[0].group
            items_name = list_items.objects.filter(name_group=group)
            items = []
            for i in items_name:
                if len(items) != 0:
                    for k in items:
                        if k != [i.nmae_item, i.FCs]:
                            items.append([i.nmae_item, i.FCs])
                else:
                    items.append([i.nmae_item, i.FCs])

            print(items)
            return render(request, 'index.html', context={"list_groups": items})
    else:
        return redirect('/login')


def display(request, name, group):
    if request.method == "GET":
        if request.session.has_key('user'):
            login = request.session['user']
            user = users.objects.filter(login=login)
            position = user[0].group
            if position == "teacher":
                work = works.objects.filter(
                    FCs=user[0].FCs, nmae_item=name, group=group)
                print(work)
                if len(work) != 0:
                    students = []
                    for obj in work:
                        stud_name = obj.FC
                        work_stud = work.filter(FC=stud_name)
                        list_work = []
                        for i in work_stud:
                            list_work.append(
                                [i.name_work, i.error, i.estimation])
                        if len(students) != 0:
                            for i in range(len(students)):
                                if students[i][0] == stud_name:
                                    pass
                                else:
                                    students.append([stud_name, list_work])
                        else:
                            students.append([stud_name, list_work])
                    return render(request, 'display.html', context={"students": students})
                else:
                    return redirect('/')
            else:
                work = works.objects.filter(
                    group=user[0].group, nmae_item=group, FC=user[0].FCs, FCs=name)
                num = list_items.objects.filter(
                    nmae_item=group, FCs=name, name_group=user[0].group)[0].quantity_works
                num_works = []
                for i in range(num):
                    num_works.append(i+1)
                print(num_works)
                return render(request, 'ship.html', context={'works': work, "num_works": num_works})
        else:
            return redirect('/login')
    else:
        if request.session.has_key('user'):
            login = request.session['user']
            user = users.objects.filter(login=login)
            link = request.POST.get('link')
            num_work = request.POST.get('num_work')
            massage = request.POST.get('message')
            work = works.objects.filter(
                nmae_item=group, FCs=name, group=user[0].group, FC=user[0].FCs, name_work=num_work)
            if len(work) == 0:
                work = works.objects.create(
                    nmae_item=group, FCs=name, group=user[0].group, FC=user[0].FCs, name_work=num_work,
                    error="-", estimation="-", message=massage, link_work=link)
            else:
                work.update(message=massage, link_work=link, error="-")
            return redirect('/'+group+'/'+name)
        else:
            return redirect('/login')


def estima(request, name, group, FC, num_work):
    if request.session.has_key('user'):
        login = request.session['user']
        user = users.objects.filter(login=login)
        if user[0].group == 'teacher':
            if request.method == "GET":
                work = works.objects.filter(
                    FCs=user[0].FCs, nmae_item=name, FC=FC, name_work=num_work, group=group)
                if len(work) != 0:
                    print(work)
                    return render(request, "estimation.html", context={"works": work})
                else:
                    return redirect("/")
            else:
                estimation = request.POST.get('estimation')
                error = request.POST.get('error')
                work = works.objects.filter(
                    FCs=user[0].FCs, nmae_item=name, FC=FC, name_work=num_work, group=group)
                work.update(error=error, estimation=estimation)
                return render(request, "estimation.html", context={"works": work})
        else:
            return redirect('/login')
    else:
        return redirect('/login')


def authorization(request):
    if request.session.has_key('user'):
        del request.session['user']
    if request.method == "GET":
        form = loging()
        return render(request, "login.html", context={"forms": form})
    else:
        form = loging(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            log = users.objects.filter(login=login, password=password)
            if len(log) != 0:
                request.session['user'] = login
                return redirect('/')
            else:
                return render(request, "login.html", context={"forms": form, "answer": "Не верный логин пароль"})


def reg_s(request):
    if request.method == "POST":
        userform = reg_stud(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            fname = userform.cleaned_data["fname"]
            group = userform.cleaned_data["group"]
            login = userform.cleaned_data["login"]
            password = userform.cleaned_data["password"]
            user = users.objects.filter(login=login)
            print(user)
            if len(user) == 0:
                user = users.objects.create(
                    FCs=str(name) + " " + str(fname), group=group, login=login, password=password)
                user.save()
                return render(request, "iget.html", {"forms": userform, "lable": "ОК"})
            else:
                return render(request, "iget.html", {"forms": userform, "lable": "Логин занят"})
        else:
            return HttpResponse("Invalid data")
    else:
        userform = reg_stud()
        return render(request, "iget.html", {"forms": userform})
