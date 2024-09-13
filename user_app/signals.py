from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    reset_password_url = "{}?token={}".format(
        instance.request.build_absolute_uri('/api/password_reset/confirm/'),
        reset_password_token.key
    )

    # Log pour vérifier si l'URL est correctement générée
    print("Generated password reset URL:", reset_password_url)

    # Ensuite, utilisez cette URL dans le contexte
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': reset_password_url
    }

    email_html_message = render_to_string('email/password_reset_email.html', context)
    email_plaintext_message = render_to_string('email/password_reset_email.txt', context)

    msg = EmailMultiAlternatives(
        "Password Reset for {title}".format(title="Your Website Title"),
        email_plaintext_message,
        "noreply@yourdomain.com",
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
