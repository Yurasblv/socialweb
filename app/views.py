from django.shortcuts import render
from app.forms import TitleForm
from app.models import GuestModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from functools import lru_cache
from django.views.decorators.http import require_http_methods, require_GET


@lru_cache()
def check_data_in_db(name):
    return GuestModel.objects.filter(name=name.lower()).exists()




@require_http_methods(["GET", "POST"])
def title_page(request):
    form = TitleForm()
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    if request.method == "POST" and is_ajax:
        form = TitleForm(request.POST)
        if form.is_valid():
            if check_data_in_db(form.data["name"]) is False:
                form.save()
                return JsonResponse({"msg": f"Hi {form.data['name']} =)",})
            return JsonResponse({'msg':f"{form.data['name']} exists yet =("})
        return JsonResponse({"msg": f"{form.errors['name'][0]}"})
    return render(request, "title.html", {"form": form})


@require_GET
def all_guests_page(request):
    guests = GuestModel.objects.order_by("id")
    paginator = Paginator(guests, 10)
    page = request.GET.get("page")
    try:
        guests = paginator.page(page)
    except PageNotAnInteger:
        guests = paginator.page(1)
    except EmptyPage:
        guests = paginator.page(paginator.num_pages)
    return render(request, "all_guests.html", {"guests": guests})
