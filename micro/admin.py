from django.contrib import admin
from django.apps import apps
from .models import Main, Service, About_us, Mics, OurClientSays, Settings, Callback, NewsLetter

admin.site.register(Main)
admin.site.register(Service)
admin.site.register(About_us)
admin.site.register(Mics)
admin.site.register(OurClientSays)
admin.site.register(Settings)
admin.site.register(Callback)
admin.site.register(NewsLetter)


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass