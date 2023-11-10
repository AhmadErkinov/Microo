from django.db import models

# Create your models here.

class Main(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    image = models.FileField(upload_to="main/", blank=True)

    book_url = models.CharField(max_length=255, blank=True)





class Service(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.FileField(upload_to="service/", blank=True)


class About_us(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    read_more_url = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to="About_us/", blank=True)

class Mics(models.Model):
    image = models.FileField(upload_to="mics/")



class OurClientSays(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()



class Settings:
    service_title = models.CharField(max_length=255)
    service_discription = models.TextField()

    our_mics_title = models.CharField(max_length=255)
    mics_description = models.TextField()

    our_client_says = models.CharField(max_length=255)
    our_client_says_description = models.TextField()

    request_callback_title = models.CharField(255)
    request_callback_content = models.TextField()

    logo = models.FileField(upload_to="settings/", blank=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=255)


    twitter_url = models.CharField(max_length=255)
    facebook_url = models.CharField(max_length=255)
    instagram_url = models.CharField(max_length=255)


class Callback(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

class NewsLetter(models.Model):
    email = models.CharField(max_length=255)