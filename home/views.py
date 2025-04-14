from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

# Create your views here.


def index(request):
    """
    A view to return the index page
    """

    return render(request, 'home/index.html')


def email_test(request):
    send_mail(
        'Test Subject',
        'This is a test email from the site.',
        settings.DEFAULT_FROM_EMAIL,
        ['ekiskarpati.dev@gmail.com'],  # 👈 change to your Gmail
        fail_silently=False,
    )
    return HttpResponse("Email sent!")
