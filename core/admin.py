
from allauth.account.models import EmailAddress
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _

from .models import Profile, Role

from django.conf.locale.en import formats as en_formats  # isort: skip
en_formats.DATE_FORMAT = "Y-m-d"  # isort: skip

admin.site.unregister(EmailAddress)
admin.site.unregister(User)


@admin.register(User)
class MyUserAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super(MyUserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.groups.filter(name='ATS Engineer').exists():
            return qs.filter(pk=request.user.pk)
        return qs.filter(is_superuser=False)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        if not request.user.is_superuser:
            fieldsets = (
                (None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {
                    'fields': ('is_active', 'is_staff', 'groups', 'user_permissions'),
                }),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
            )
            if request.user.groups.filter(name='ATS Engineer').exists():
                return (
                    (None, {'fields': ('username', 'password')}),
                    (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                )
            return fieldsets
        else:
            return self.fieldsets


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'created_by',
        'created_at',
        'modified_by',
        'modified_at',
    ]
    search_fields = ['name']
    ordering = ['created_at']
    fields = ('name',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'role',
        'timezone',
    ]
    search_fields = ['user__first_name', 'user__last_name', 'user__email', 'role__name']
    ordering = ['user__username']

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'user':
            kwargs['queryset'] = get_user_model().objects.filter(is_superuser=False)
        return super(ProfileAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
