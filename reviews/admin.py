# review model adopted from https://github.com/gomathishankar28/ms4_bubbles
from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'product',
        'user',
        'rating',
        'review_date'
    )
