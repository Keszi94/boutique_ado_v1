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
    from_email = settings.DEFAULT_FROM_EMAIL
    print("Sending email from:", from_email) 

    send_mail(
        'Test Subject',
        'This is a test email from the site.',
        from_email,
        ['ekiskarpati.dev@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("Email sent!")

