from django.contrib import admin

from lives.models import Program, Host


# Register your models here.
class HostInline(admin.TabularInline):
    model = Host
    extra = 1


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    inlines = [
        HostInline,
    ]


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
