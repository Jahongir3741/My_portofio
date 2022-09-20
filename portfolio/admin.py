from django.contrib import admin
from .models import Contact, Networks,Author,Skills,Resume,Text

@admin.register(Contact)
class ContacAdmin(admin.ModelAdmin):
  search_fields=("your_name","subject")
  list_display=("your_name","subject","your_email")
  list_filter = ("your_name",)

admin.site.register((Networks,Author,Skills,Resume,Text))
