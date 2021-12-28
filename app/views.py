from django.shortcuts import render
from app.forms import TitleForm
from app.models import GuestModel
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def title_page(request):
    form = TitleForm()
    if request.method == 'POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            guest = GuestModel.objects.filter(name=form.data['name']).first()
            if guest is None:
                guest = GuestModel.objects.create(name=form.data['name'])
                guest.save()
                return redirect('guests')
            else:
                messages.error(request,'User already exists')
                return redirect('title')
        return render(request, 'title.html', {'form': form})
    return render(request, 'title.html', {'form': form})


def all_guests_page(request):
    guests = GuestModel.objects.order_by('id')
    paginator = Paginator(guests, 15)
    page = request.GET.get('page')
    try:
        guests = paginator.page(page)
    except PageNotAnInteger:
        guests = paginator.page(1)
    except EmptyPage:
        guests = paginator.page(paginator.num_pages)
    return render(request, 'all_guests.html', {'guests': guests})
