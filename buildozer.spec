[app]
title = FitMaster Pro
package.name = fitmaster
package.domain = org.dinanafezi

source.dir = .
source.include_exts = py,html,css,js,json,webp,png,jpg,jpeg,svg,ico,ttf,otf,woff,woff2

version = 1.0.0
requirements = python3,kivy,pyjnius,android

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk_api = 24
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
