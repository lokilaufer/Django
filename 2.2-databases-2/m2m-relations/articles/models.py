from django.db import models
from django.forms import BaseInlineFormSet
from werkzeug.routing import ValidationError

from orm_migrations.school import admin


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    tags = models.ManyToManyField(Tag, through='Scope')

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.article.title} - {self.tag.name}'


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_count += 1
                if main_count > 1:
                    raise ValidationError('Only one main scope is allowed per article')
        if main_count == 0:
            raise ValidationError('One main scope is required per article')
        return super().clean()



