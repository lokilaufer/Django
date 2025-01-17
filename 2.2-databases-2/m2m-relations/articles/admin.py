from django.contrib import admin

from .models import Article, ScopeInlineFormset, Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    class ScopeInline(admin.TabularInline):
        model = Scope
        formset = ScopeInlineFormset

        class Meta:
            ordering = ['-published_at']
