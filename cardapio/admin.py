from django.contrib import admin
from . import models


class CardapioAdmin(admin.ModelAdmin):
    exclude = ["slug"]

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return ['semana']

admin.site.register(models.Cardapio, CardapioAdmin)

