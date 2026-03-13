[app]

title = FoodApp
package.name = foodapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0

# Android config
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

android.accept_sdk_license = True

# Fix lỗi build phổ biến
p4a.bootstrap = sdl2

[buildozer]

log_level = 2
warn_on_root = 1
