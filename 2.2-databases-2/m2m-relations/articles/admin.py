from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag

class TagshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                is_main += 1

                if is_main > 1:
                    raise ValidationError('Основной тег должен быть один')

        if is_main == 0:
            raise ValidationError('Выберите основной тег')

        return super().clean()

class TagshipInline(admin.TabularInline):
    model = Tag.articles.through
    formset = TagshipInlineFormset
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagshipInline]

