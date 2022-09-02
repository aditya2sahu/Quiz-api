from django.contrib import admin
from.models import Questions,Quiz,Answer




class Ansinline(admin.TabularInline):
    model = Answer





class Questionsadmin(admin.ModelAdmin):
    inlines = [Ansinline]
    class Meta:
        model= Questions

admin.site.register(Questions,Questionsadmin)
admin.site.register(Answer)
admin.site.register(Quiz)




