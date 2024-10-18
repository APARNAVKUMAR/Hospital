from .models import Department, News, Booking

from django.contrib import admin
# Register your models here.
admin.site.register(Department)
admin.site.register(News)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_dep', 'book_date', 'book_phn')
admin.site.register(Booking, BookingAdmin)