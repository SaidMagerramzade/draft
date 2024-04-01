
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView, FormView, DeleteView
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse, request
from django.core.serializers import serialize
from django.urls import reverse, reverse_lazy
from .forms import CakeForm, EmailForm
from .models import Cake
from mail.models import Mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


# def index(request):
#     cakes = Cake.objects.all()
#     #price = request.GET.get("price")
#     price_min = request.GET.get("price_min")
#     price_max = request.GET.get("price_max")
#     print(f"{price_min=}")
#     print(f"{price_max=}")
#     print(request.GET)
#     if price_min:
#         cakes = cakes.filter(price__gte=price_min)
#     if price_max:
#         cakes = cakes.filter(price__lte=price_max)
#     context = {
#         "cakes": cakes
#     }
#     return render(request, "cakes/home.html", context)


"""def index_view(request):
    cakes = Cake.objects.order_by("price")
    context = {
        "cakes": cakes
    }
    return render(request, "cakes/home.html", context)
"""
class IndexView(LoginRequiredMixin, ListView):
    model = Cake
    template_name = "cakes/home.html"
    context_object_name = "cakes"

    def get_queryset(self):
        queryset = super().get_queryset()
        price_min = self.request.GET.get("price_min")
        price_max = self.request.GET.get("price_max")

        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        return queryset

def cake_detail_view(request, pk, slug):
    cake = Cake.objects.get(pk=pk)
    context ={
        "cake": cake
    }
    return render(request, "cakes/cake_details.html", context)

class CakeDetailView(LoginRequiredMixin, DetailView):
    model = Cake
    template_name = "cakes/cake_details.html"
    context_object_name = "cake"


class AboutView(LoginRequiredMixin, ListView):
    model = Cake
    template_name = "cakes/about.html"
    context_object_name = "cakes"

class ContactsView(LoginRequiredMixin, ListView):
    model = Cake
    template_name = "cakes/contacts.html"
    context_object_name = "cakes"


class json(ListView):
    model = Cake

    def get_queryset(self):
        queryset = super().get_queryset()
        price_min = request.GET.get("price_min")
        price_max = request.GET.get("price_max")
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
            return queryset
    
    def render_to_response(self, context, **response_kwargs):
        data = serialize("json", context['object_list'])
        return JsonResponse(data, safe=False)





"""def json(request):
    cakes = Cake.objects.all()
    price_min = request.GET.get("price_min")
    price_max = request.GET.get("price_max")
    print(f"{price_min=}")
    print(f"{price_max=}")
    print(request.GET)
    if price_min:
         cakes = cakes.filter(price__gte=price_min)
    if price_max:
         cakes = cakes.filter(price__lte=price_max)
    data = serialize("json", cakes)
    return  JsonResponse(data, safe=False)"""

class LatestCakeView(LoginRequiredMixin, ListView):
    model = Cake
    template_name = "cakes/latest.html"
    context_object_name = "cakes"

    def get_queryset(self):
        last_cake = super().get_queryset()
        last_cake = last_cake.order_by("-baked_at")[:5]
        return last_cake


"""def latest_cakes_view(request):
    cakes = Cake.objects.order_by("-baked_at")[:5]
    context = {
        "cakes": cakes
    }
    return render(request, "cakes/latest.html", context)"""


"""def create_cake_view(request):
    if request.method == "POST":
        tortun_adi = request.POST.get("name")
        description = request.POST.get("description")
        weight = request.POST.get("weight")
        price = request.POST.get("price")
        image = request.FILES.get("image")
        Cake.objects.create(
            name=tortun_adi,
            description=description,
            weight=weight,
            price=price,
            image=image
        )
        email = request.user.email
        send_mail(
            'Hello',
            "Thanks for using our service",
            settings.EMAIL_HOST_USER,
            [email],
            )
        print(request.FILES)
        return redirect("/")
    return render(request, 'cakes/new_cake.html')"""


"""def send_mail_view(request):
    if request.method == "POST":
        address = request.POST.get("address")
        title = request.POST.get("title")
        message = request.POST.get("message")
        send_mail(
                title,
                message,
                settings.EMAIL_HOST_USER,
                [address],
            )
        return HttpResponseRedirect("/success/")
    return render(request, 'cakes/email_form.html')"""



def success_view(request):
    return render(request, "cakes/success.html")


class CreateCakeView(LoginRequiredMixin, FormView):
    form_class = CakeForm
    template_name = 'cakes/new_cake.html'
    success_url = reverse_lazy('cakes:success')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        weight = form.cleaned_data['weight']
        price = form.cleaned_data['price']
        image = form.cleaned_data['image']
        stars = form.cleaned_data['stars']
        print(form.cleaned_data)

        Cake.objects.create(
            name=name,
            description=description,
            weight=weight,
            price=price,
            image=image,
            stars=stars
        )
        email = self.request.user.email
        title = "Hello"
        message = "Thanks for using our service"
        mail = EmailMessage(
            title,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            )
        mail.send()

        Mail.objects.create(
            address=email,
            title=title,
            message=message
        )
        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse('cakes:success')

class SendMailView(LoginRequiredMixin, FormView):
    form_class = EmailForm
    template_name = 'cakes/email_form.html'

    def form_valid(self, form):
        address = form.cleaned_data["address"]
        title = form.cleaned_data["title"]
        message = form.cleaned_data["message"]

        email = EmailMessage(
            title,
            message,
            settings.EMAIL_HOST_USER,
            [address],
        )
        email.send()
        return super().form_valid(form)
    
    """def get_success_url(self):
        return reverse('cakes:success')"""

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CakeDeleteView(LoginRequiredMixin, DeleteView):
    model = Cake
    success_url = reverse_lazy("cakes:success")

"""def delete_cake_view(request, pk):
    delete_cake = Cake.objects.get(pk=pk)
    delete_cake.delete()
    return redirect("/")"""

class CakeRatingView(LoginRequiredMixin, ListView):
    model = Cake
    template_name = "cakes/rating.html"
    context_object_name = "cakes"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(stars__gte=1)
        return queryset

    
