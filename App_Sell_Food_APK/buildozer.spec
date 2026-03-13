[app]

title = FoodApp
package.name = foodapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy==2.2.1,pyjnius==1.5.0

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21

android.ndk = 25c
android.ndk_api = 21
android.archs = arm64-v8a

p4a.bootstrap = sdl2
android.accept_sdk_license = True


[buildozer]

log_level = 2
warn_on_root = 1
