from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from micro.models import Main, Service, About_us, Mics, OurClientSays, Settings, Callback, NewsLetter


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["main"] = Main.objects.all()[:4] 
        context["about_us"] = About_us.objects.all()[all]
        context["service"] = Service.objects.all()[all]

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class ServicesView(TemplateView):
    template_name = "wervices.html"

class ShopView(TemplateView):
    template_name = "shop.html"


