from django.shortcuts import render
from .models import AppVersion, HeroScreenshot, Logo

def home(request):
    customer_app = AppVersion.objects.filter(name__icontains='مشتری').first()
    barber_app = AppVersion.objects.filter(name__icontains='آرایشگر').first()
    screenshot_left = HeroScreenshot.objects.filter(position='left').first()
    screenshot_right = HeroScreenshot.objects.filter(position='right').first()
    logo = Logo.objects.first()

    context = {
        'customer_app': customer_app,
        'barber_app': barber_app,
        'screenshot_left': screenshot_left,
        'screenshot_right': screenshot_right,
        'logo': logo,
    }
    return render(request, 'ariacuts.html', context)