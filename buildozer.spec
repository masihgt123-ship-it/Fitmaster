[app]

# عنوان برنامه
title = FitMaster Pro

# نام پکیج؛ فقط حروف کوچک و عدد
package.name = fitmaster

# دامنهٔ پکیج
package.domain = org.dinanafezi

# پوشه‌ای که main.py داخل آن قرار دارد
source.dir = .

# پسوند فایل‌هایی که باید وارد برنامه شوند
source.include_exts = py,kv,atlas,html,css,js,json,png,jpg,jpeg,webp,svg,ttf,otf,woff,woff2,txt

# نسخهٔ برنامه
version = 0.1

# نیازمندی‌های برنامه
requirements = python3,kivy,pyjnius,android

# جهت صفحه (عمودی)
orientation = portrait

# تمام‌صفحه نباشد
fullscreen = 0

# مجوزهای اندروید
android.permissions = INTERNET

# نسخهٔ هدف و تنظیمات بیلد اندروید
android.api = 34
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

# آیکون روی صفحه اصلی گوشی
icon.filename = %(source.dir)s/icon-192.png

# تصویر صفحهٔ بارگذاری ابتدایی (مرحله ۲)
presplash.filename = %(source.dir)s/icon-512.png

# رنگ پس‌زمینهٔ صفحه بارگذاری (دقیقاً رنگ زمینه تیره فیت‌مستر تا پرش رنگی نداشته باشی)
android.presplash_color = #07111f

p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 0
