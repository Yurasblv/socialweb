from django.shortcuts import render
from app.forms import TitleForm
from app.models import GuestModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_GET
from django.core.cache import cache


def check_data_in_db(name):
    cached_name = cache.get(name)
    if not cached_name:
        cached_name = GuestModel.objects.filter(name=name).exists()
        if cached_name:
            cache.set(name, cached_name)
    return cached_name


@require_http_methods(["GET", "POST"])
def title_page(request):
    form = TitleForm()
    if request.method == "POST":
        form = TitleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if check_data_in_db(name) is False:
                form.save(name)
                return JsonResponse(
                    {
                        "msg": f"Hi {form.data['name']} =)",
                    }
                )
            return JsonResponse({"msg": f"{form.data['name']} exists yet =("})
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
