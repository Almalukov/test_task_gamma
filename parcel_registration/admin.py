from django.contrib import admin
from .models import Letter, Parcel

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'recipient_name', 'letter_type', 'letter_weight')
    list_filter = ('letter_type',)
    search_fields = ('sender_name', 'recipient_name', 'sending_location', 'receiving_location')

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'recipient_name', 'parcel_type', 'payment_amount')
    list_filter = ('parcel_type',)
    search_fields = ('sender_name', 'recipient_name', 'sending_location', 'receiving_location', 'notification_phone')
