from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'created_at', 'subscribe_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('paid', 'created_at')
    actions = ['mark_as_paid']

    def subscribe_today(selfself, obj):
        return obj.created_at == now().date()

    def mark_as_paid(self, request, queryset):
        queryset.update(paid=True)

    mark_as_paid.short_description = 'Marcar como pago'
    subscribe_today.short_description = 'inscrito hoje?'
    subscribe_today.boolean = True

admin.site.register(Subscription)
