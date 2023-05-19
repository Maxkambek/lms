from django.contrib import admin
from .models import Timetable, Subject, Group, GroupMembers


class GroupMembersAdmin(admin.StackedInline):
    model = GroupMembers
    extra = 1


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupMembersAdmin]
    search_fields = ['name']


admin.site.register(Timetable)
admin.site.register(Subject)
