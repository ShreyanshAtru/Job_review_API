from django.contrib import admin
from .models import Candidate
# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','status']

admin.site.register(Candidate, CandidateAdmin)
