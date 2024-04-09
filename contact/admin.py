from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    readonly_fields = (
        'contact_name',
        'contact_email',
        'contact_message',
        'date',
    )

    fields = (
        'contact_email',
        'date',
        'contact_name',
        'contact_subject',
        'contact_message',
        'have_replied',
    )

    list_display = (
        'contact_email',
        'contact_name',
        'date',
        'have_replied',
    )

    ordering = ('-date',)


admin.site.register(ContactForm, ContactFormAdmin)
