from django.contrib import admin
from .models import User, Endereco

class EnderecosInLine(admin.StackedInline):
    model = Endereco
    extra = 0

class UserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'is_staff', 'is_active')
    list_filter = ['is_staff', 'is_active']

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'password', 'email')
        }),
        ('Opções avançadas', {
            'classes': ('collapse',),
            'fields': (('is_staff', 'is_active'), 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    inlines = [EnderecosInLine]

admin.site.register(User, UserAdmin)