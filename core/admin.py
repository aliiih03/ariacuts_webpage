from django.contrib import admin
from .models import AppVersion, HeroScreenshot, Logo

@admin.register(AppVersion)
class AppVersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')

@admin.register(HeroScreenshot)
class HeroScreenshotAdmin(admin.ModelAdmin):
    list_display = ('position', 'image')

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('image',)