from django.shortcuts import render
from app.forms import TitleForm
from app.models import GuestModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from functools import lru_cache


@lru_cache(maxsize=100)
def check_data_in_db(name):
    return GuestModel.objects.filter(name=name).exists()


def title_page(request):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    form = TitleForm()
    if is_ajax:
        form = TitleForm()
        if request.method == "POST":
            form = TitleForm(request.POST)
            if form.is_valid():
                guest = check_data_in_db(form.data["name"])
                if guest is False:
                    form.save()
                    return JsonResponse(
                        {
                            "msg": f"Hi {form.data['name']} =)",
                        }
                    )
                return JsonResponse({"msg": f"{form.data['name']} already exists =]"})
            return JsonResponse(
                {"msg": f"{form.data['name']} not allowed ," f"wrong format of name!"}
            )
    return render(request, "title.html", {"form": form})


def all_guests_page(request):
    guests = GuestModel.objects.order_by("id")
    paginator = Paginator(guests, 15)
    page = request.GET.get("page")
    try:
        guests = paginator.page(page)
    except PageNotAnInteger:
        guests = paginator.page(1)
    except EmptyPage:
        guests = paginator.page(paginator.num_pages)
    return render(request, "all_guests.html", {"guests": guests})
