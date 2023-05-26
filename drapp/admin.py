from django.contrib import admin
from .models import *
# admin.site.register(Instructor)
# admin.site.register(Student)
# admin.site.register(Payment)
# admin.site.register(Slot)
# admin.site.register(Bookslot)
from django.utils.html import format_html
# Register your models here.
class InstructorsAdmin(admin.ModelAdmin):
    list_display = ('display_photo','first_name', 'is_verified', 'view_license_button')
   
    def view_license_button(self, obj):
        url = reverse('view_license', args=[obj.pk])
        return format_html('<b><a class="button" href="{}">View License</a></b>', url)

    def display_photo(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))

    display_photo.short_description = 'logo'
    view_license_button.short_description = ''

    def verify_license(self, request, queryset):
        for provider in queryset:
            provider.status = 'Verified'
            provider.is_verified = True
            provider.save()

    verify_license.short_description = "Verify selected Instructors licenses"

    actions = [verify_license]

admin.site.register(Instructor, InstructorsAdmin)

from django.contrib import admin
from .models import Student


from django.utils.html import format_html

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('display_image','first_name', 'last_name', 'email', 'address')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return ''

    display_image.short_description = 'Image'


from django.contrib import admin
from .models import Slot


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'slottime', 'status')
from django.contrib import admin
from .models import Bookslot


@admin.register(Bookslot)
class BookslotAdmin(admin.ModelAdmin):
    list_display = ('student', 'slot', 'instructor', 'status')


