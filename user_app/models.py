from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username


# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
#     email_plaintext_message= "{}?token={}".format(reverse('password_reset:reset-password-request'),reset_password_token.key)

#     send_mail(
#         #title
#         "Password Reset for {title}".format(titlr="Burundi en Temps Réel")
#         #message:
#         email_plaintext_message
#         #from:
#         "nkurunzizajeandarc@gmail.com"
#         #to :
#         [reset_password_token.user.email]

#     )
