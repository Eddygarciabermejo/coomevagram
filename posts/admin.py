from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Post admin """

    list_display = ('pk', 'user_link', 'title', 'photo')
    readonly_fields = ('user_link', )
    list_editable = ('title', )
    search_fields = ('title', 'photo', 'user__username')
    list_filter = ('created', 'modified')

    def user_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:auth_user_change", args=(obj.user.pk,)),
            obj.user.username
        ))

    user_link.short_description = 'user'
