from django.contrib import admin
from django.contrib.admin.helpers import AdminForm
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """Review Admin Definition"""

    pass
