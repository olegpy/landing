from django.contrib import admin

from .models import Thumbnail, MainSlider, Review


class ThumbnailAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Field For image', {'fields': ['image']}),
        ('Header Thumbnail', {'fields': ['header']}),
        ('Description', {'fields': ['description']})
    ]


class MainSliderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Field For image', {'fields': ['image']}),
        ('Header Slider', {'fields': ['header']}),
        ('Description', {'fields': ['description', 'btn_text']})
    ]


class ReviewAdmin(admin.ModelAdmin):
    list_filter = ['author']
    fieldsets = [
        ('Field For image and video', {'fields': ['image', 'url_video']}),
        ('Name author', {'fields': ['author']}),
        ('Text', {'fields': ['header', 'description']})
    ]

admin.site.register(Thumbnail, ThumbnailAdmin)
admin.site.register(MainSlider, MainSliderAdmin)
admin.site.register(Review, ReviewAdmin)

# Register your models here.
