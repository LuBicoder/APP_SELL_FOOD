[app]

title = FoodApp
package.name = foodapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

# thêm dòng này để GitHub tự chấp nhận license
android.accept_sdk_license = True

# thêm cấu hình Android để tránh lỗi build tools
android.api = 33
android.minapi = 21
android.ndk = 25b

[buildozer]

log_level = 2
warn_on_root = 1
