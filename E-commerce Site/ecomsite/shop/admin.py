from django.contrib import admin
from .models import Product
# Register your models here.
admin.site.site_header = 'E-commerce site'
admin.site.site_title = "ABC Shop"
admin.site.index_title = 'Manage ABC Shopping'

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category="Default") 

    change_category_to_default.short_description = 'Default category'
    list_display = ('title', 'price', 'discount_price', 'category')
    search_fields = ("title",'category')
    actions = ("change_category_to_default",)

    # fields = ('title','price')
    list_editable = ('price','discount_price',)


admin.site.register(Product,ProductAdmin)

