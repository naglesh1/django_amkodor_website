from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from .models import News, Contact, Vacancy, Tender, Rent, Products, ProductCategory, Nelekvidi, TransportBY, Services



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content', 'photo', 'post_photo')
    list_display = ('title', 'post_photo', 'time_create', 'is_published')
    list_display_links = ('title',)
    ordering = ['-time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 10

    search_fields = ['title__iregex']
    list_filter = ['is_published']
    actions = ['set_published', 'del_published']

    readonly_fields = ('post_photo',)
    prepopulated_fields = {'slug': ('title',)}

    @admin.display(description='Изображение')
    def post_photo(self, new: News):
        if new.photo:
            return mark_safe(f"<img src='{new.photo.url}' width=50>")
        return f'Без фото'

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=News.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей')

    @admin.action(description='Снять с публикации выбранные записи')
    def del_published(self, request, queryset):
        count = queryset.update(is_published=News.Status.DRAFT)
        self.message_user(request, f'Изменено {count} записей')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('title', 'name', 'telephone', 'faks', 'email', 'advantage')
    list_display = ('title', 'name', 'email', 'advantage')
    list_display_links = ('title',)
    ordering = ['advantage', 'title']
    list_editable = ('advantage',)

    list_per_page = 10
    search_fields = ['title__iregex']
    list_filter = ('title',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title',)

    list_per_page = 10
    search_fields = ['title__iregex']

    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    list_per_page = 10

    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title__iregex']


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('content',)
    list_display_links = ('content',)
    list_per_page = 10


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    list_per_page = 10

    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name__iregex']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'category', 'content', 'photo', 'post_photo', 'photo2', 'photo3', 'file')
    list_display = ('title', 'post_photo', 'category', 'time_create',)
    list_display_links = ('title',)
    ordering = ['-time_create', 'title']
    list_editable = ('category',)
    list_per_page = 10

    search_fields = ['title__iregex']

    readonly_fields = ('post_photo',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title__iregex']
    list_filter = ['category']

    @admin.display(description='Изображение')
    def post_photo(self, new: News):
        if new.photo:
            return mark_safe(f"<img src='{new.photo.url}' width=50>")
        return f'Без фото'


@admin.register(Nelekvidi)
class NelecvidiAdmin(admin.ModelAdmin):
    list_display = ('title', 'eng')
    search_fields = ['title__iregex']
    ordering = ['title']


@admin.register(TransportBY)
class TransportBYAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content', 'photo', 'post_photo', 'photo2', 'photo3',)
    list_display = ('title', 'post_photo', 'time_create',)
    list_display_links = ('title',)
    ordering = ['-time_create', 'title']

    list_per_page = 10

    search_fields = ['title__iregex']

    readonly_fields = ('post_photo',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title__iregex']

    @admin.display(description='Изображение')
    def post_photo(self, new: News):
        if new.photo:
            return mark_safe(f"<img src='{new.photo.url}' width=50>")
        return f'Без фото'


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content', 'photo', 'post_photo', 'file')
    list_display = ('title', 'post_photo', 'slug')
    list_display_links = ('title',)
    ordering = ['title']

    list_per_page = 10

    search_fields = ['title__iregex']

    readonly_fields = ('post_photo',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title__iregex']

    @admin.display(description='Изображение')
    def post_photo(self, new: News):
        if new.photo:
            return mark_safe(f"<img src='{new.photo.url}' width=50>")
        return f'Без фото'


