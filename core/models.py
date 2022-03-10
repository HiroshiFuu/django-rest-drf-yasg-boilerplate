from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

from .middleware import get_current_user

from phonenumber_field.modelfields import PhoneNumberField

from .timezones import DEFAULT_TIMEZONE, TIMEZONE_CHOICES


class AuditMixin(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(editable=False, auto_now_add=True, verbose_name='Created At')
    modified_at = models.DateTimeField(blank=True, null=True, verbose_name='Modified At')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='%(class)s_created', editable=False, verbose_name='Created By')
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='%(class)s_modified', blank=True, null=True, verbose_name='Modified By')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
            if not getattr(self, 'created_by', None):
                self.created_by = get_current_user()
        else:
            self.modified_at = timezone.now()
            if not getattr(self, 'modified_by', None):
                self.modified_by = get_current_user()
        return super().save(*args, **kwargs)


class Role(AuditMixin):
    name = models.CharField('Role Name', max_length=63, unique=True)

    class Meta:
        managed = True
        verbose_name = 'Role'

    def __str__(self):
        return '{}'.format(self.name)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='profiles')
    phone_number = PhoneNumberField('Phone Number', null=True, blank=True)
    timezone = models.CharField('Timezone', max_length=63, choices=TIMEZONE_CHOICES, default=DEFAULT_TIMEZONE)

    @property
    def fullname(self):
        return self.user.first_name + ' ' + self.user.last_name
