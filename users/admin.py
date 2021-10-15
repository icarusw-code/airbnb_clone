from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(UserAdmin):

    """Custom User Admin"""

    # 장고 filedsets 와 내가 만든거을 합쳐준다.
    fieldsets = UserAdmin.fieldsets + (
        (
            # 파란색의 타이틀
            "Custom Profile",
            {
                # 파란색 밑의 내용
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
