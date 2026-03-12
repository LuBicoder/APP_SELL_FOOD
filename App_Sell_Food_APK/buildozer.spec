[app]

# Tên ứng dụng
title = FoodApp

# ID ứng dụng
package.name = foodapp
package.domain = org.test

# Thư mục source
source.dir = .

# File được include
source.include_exts = py,png,jpg,kv

# Version app
version = 1.0

# Thư viện cần dùng
requirements = python3,kivy==2.2.1,openssl,sqlite3

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Chấp nhận license Android SDK
android.accept_sdk_license = True

# Cấu hình Android ổn định cho GitHub
android.api = 31
android.minapi = 21
android.ndk = 25b

# Kiến trúc build
android.archs = arm64-v8a, armeabi-v7a

# Bootstrap cho Kivy
p4a.bootstrap = sdl2

# Icon (nếu có)
# icon.filename = %(source.dir)s/icon.png

# Splash screen (nếu có)
# presplash.filename = %(source.dir)s/presplash.png


[buildozer]

# Level log
log_level = 2

# Cảnh báo root
warn_on_root = 1
