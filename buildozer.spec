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

# جهت صفحه
orientation = portrait

# تمام‌صفحه نباشد
fullscreen = 0

# مجوزهای اندروید
android.permissions = INTERNET

# نسخهٔ هدف اندروید
android.api = 34

# کمترین نسخهٔ اندروید پشتیبانی‌شده
android.minapi = 24

# نسخهٔ API برای NDK
android.ndk_api = 24

# تنظیم SDK اندروید
android.skip_update = False
android.accept_sdk_license = True

# معماری خروجی APK
android.archs = arm64-v8a


[buildozer]

# سطح نمایش گزارش‌های ساخت
log_level = 2

# نمایش هشدار در صورت اجرای Buildozer با دسترسی ریشه
warn_on_root = 1
