from django.contrib import admin
from .models import Articl, Comments, Category, Reviews, News, Place
# from modeltranslation.admin import TranslationAdmin
from simple_history.admin import SimpleHistoryAdmin

class ArticlAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id' , 'title' , 'data' , 'is_published')
    list_display_links = ('id' , 'title' )
    search_fields = ('title' , 'full_text')

class CategoryAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id' , 'name')
    list_display_links = ('id' , 'name' )
    search_fields = ('name' , 'name')

class CommentsAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id' , 'author', 'data', 'text', 'status')
    list_display_links = ('id' , 'author', 'data', 'text', 'status' )
    search_fields = ('text' , 'text')

class ReviewsAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id' , 'text', 'data')
    list_display_links = ('id' , 'text', 'data')
    search_fields = ('text' , 'text')

class NewsAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id' , 'text', 'data')
    list_display_links = ('id' , 'text', 'data')
    search_fields = ('text' , 'text')

class PlaceAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id' , 'text')
    list_display_links = ('id' , 'text')
    search_fields = ('text' , 'text')

admin.site.register(Articl, ArticlAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Place, PlaceAdmin)

admin.site.site_title = 'Админ-панель сайта "Вакансии"' 
admin.site.site_header = 'Админ-панель сайта "Вакансии"'
