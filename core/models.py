from django.db import models

class AppVersion(models.Model):
    name = models.CharField(max_length=100)  # مثلاً "نسخه مشتری" یا "نسخه آرایشگر"
    file = models.FileField(upload_to='apps/')  # فایل APK یا هرچی
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class HeroScreenshot(models.Model):
    position = models.CharField(max_length=10, choices=[('left', 'چپ'), ('right', 'راست')])  # برای دو تا گوشی
    image = models.ImageField(upload_to='screenshots/')

    def __str__(self):
        return f"اسکرین‌شات {self.position}"

class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')

    def __str__(self):
        return "لوگو سایت"



